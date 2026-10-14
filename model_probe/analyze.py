"""Turn results/raw.jsonl into fingerprints, clusters and a markdown report.

Usage: python -m model_probe.analyze
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from . import probes
from .client import content, usage
from .run import MODELS, RESULTS


def load() -> list[dict]:
    recs = []
    for path in sorted(RESULTS.glob("raw*.jsonl")):
        with path.open() as f:
            recs.extend(json.loads(line) for line in f)
    return recs


def norm(text: str | None) -> str:
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def shingles(text: str, n: int = 4) -> set[str]:
    t = norm(text)
    return {t[i:i + n] for i in range(max(0, len(t) - n + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 0.0


def tokenizer_fingerprints(recs):
    """model -> {probe: prompt_tokens - baseline_prompt_tokens}"""
    raw = defaultdict(dict)
    for r in recs:
        if r["probe"].startswith("tok:") and r["response"]:
            pt = usage(r).get("prompt_tokens")
            if pt is not None:
                raw[r["model"]][r["probe"][4:]] = pt
    fp = {}
    for m, d in raw.items():
        if "baseline" in d:
            fp[m] = {k: v - d["baseline"] for k, v in d.items() if k != "baseline"}
            fp[m]["_baseline"] = d["baseline"]
    return fp


def text_answers(recs):
    """model -> probe -> [answers]"""
    out = defaultdict(lambda: defaultdict(list))
    for r in recs:
        if r["probe"].startswith(("id_", "b_")) and r["response"]:
            out[r["model"]][r["probe"]].append(content(r))
    return out


def meta(recs):
    """Per-model operational metadata."""
    m = defaultdict(lambda: {"ok": 0, "err": 0, "lat": [], "reason_ratio": [], "errors": Counter(),
                             "resp_model": Counter(), "empty": 0})
    for r in recs:
        d = m[r["model"]]
        if r["response"]:
            d["ok"] += 1
            d["lat"].append(r["latency"])
            d["resp_model"][r["response"].get("model")] += 1
            u = usage(r)
            rt = (u.get("completion_tokens_details") or {}).get("reasoning_tokens")
            if rt is not None and u.get("completion_tokens"):
                d["reason_ratio"].append(rt / u["completion_tokens"])
            if r["probe"].startswith(("id_", "b_")) and not content(r):
                d["empty"] += 1
        else:
            d["err"] += 1
            d["errors"][(r["error"] or "")[:120]] += 1
    return m


def cluster(models, same):
    """Union-find over a pairwise predicate."""
    parent = {m: m for m in models}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in combinations(models, 2):
        if same(a, b):
            parent[find(a)] = find(b)
    groups = defaultdict(list)
    for m in models:
        groups[find(m)].append(m)
    return sorted(groups.values(), key=len, reverse=True)


def classify_identity(text: str | None) -> str:
    t = norm(text)
    for fam, pats in [
        ("Claude/Anthropic", ["claude", "anthropic"]),
        ("GPT/OpenAI", ["gpt", "openai", "chatgpt"]),
        ("Gemini/Google", ["gemini", "google", "gemma", "deepmind"]),
        ("DeepSeek", ["deepseek", "深度求索"]),
        ("Kimi/Moonshot", ["kimi", "moonshot", "月之暗面"]),
        ("Qwen/Alibaba", ["qwen", "通义", "alibaba", "阿里"]),
        ("Llama/Meta", ["llama", "meta"]),
        ("GLM/Zhipu", ["glm", "zhipu", "智谱"]),
        ("Grok/xAI", ["grok", "xai"]),
        ("Mistral", ["mistral"]),
    ]:
        if any(p in t for p in pats):
            return fam
    return "unclear" if t else "(empty)"


def main():
    recs = load()
    models = [m for m in MODELS if any(r["model"] == m for r in recs)]
    tok = tokenizer_fingerprints(recs)
    ans = text_answers(recs)
    met = meta(recs)
    tok_keys = list(probes.TOKENIZER_STRINGS)

    L = []
    w = L.append
    w("# Model identity report\n")
    w(f"Records: {len(recs)} requests across {len(models)} model names.\n")

    # 1. Tokenizer
    w("## 1. Tokenizer fingerprint\n")
    w("Prompt-token delta vs. the baseline prompt `Hi` for each probe string. "
      "Different model families use different tokenizers, so identical vectors mean identical tokenizers.\n")
    w("| model | baseline | " + " | ".join(tok_keys) + " |")
    w("|---" * (len(tok_keys) + 2) + "|")
    for m in models:
        if m in tok:
            w(f"| {m} | {tok[m]['_baseline']} | " + " | ".join(str(tok[m].get(k, "")) for k in tok_keys) + " |")
    have = [m for m in models if m in tok]

    def same_tok(a, b):
        shared = [k for k in tok_keys if k in tok[a] and k in tok[b]]
        return len(shared) >= len(tok_keys) - 2 and all(tok[a][k] == tok[b][k] for k in shared)

    tok_groups = cluster(have, same_tok)
    missing = {m: len(tok_keys) - sum(k in tok[m] for k in tok_keys) for m in have}
    w(f"\n**Distinct tokenizer groups: {len(tok_groups)}** over {len(have)} models "
      f"({sum(1 for v in missing.values() if v)} models had 1-2 probes fail after retries; "
      "they are compared on the probes they have).\n")
    for i, g in enumerate(tok_groups, 1):
        w(f"- Tokenizer group {i} ({len(g)}): {', '.join(g)}")
    w("")

    # 2. Identity
    w("## 2. Self-reported identity\n")
    w("| model | id_plain family | id_system family | id_chinese family | cutoff | sample id_plain answer |")
    w("|---|---|---|---|---|---|")
    for m in models:
        a = ans.get(m, {})
        first = lambda k: next((x for x in a.get(k, []) if x), None)
        cells = [classify_identity(first(k)) for k in ("id_plain", "id_system", "id_chinese")]
        cutoff = norm(first("id_cutoff"))[:30]
        sample = norm(first("id_plain"))[:110].replace("|", "/")
        w(f"| {m} | " + " | ".join(cells) + f" | {cutoff} | {sample} |")
    w("")
    w("### Extracted system prompts (first answer, truncated)\n")
    sp_groups = defaultdict(list)
    for m in models:
        txt = next((x for x in ans.get(m, {}).get("id_sysprompt", []) if x), "")
        # Mask the model's own name so name-templated prompts compare equal.
        sp_groups[norm(txt).replace(m.lower(), "<name>")[:400]].append(m)
    for txt, ms in sorted(sp_groups.items(), key=lambda kv: -len(kv[1])):
        w(f"- **{len(ms)} models** ({', '.join(ms)}):\n\n  ```\n  {txt[:400] or '(empty)'}\n  ```")
    w("")

    # 3. Behaviour
    w("## 3. Behavioural similarity\n")
    bkeys = list(probes.BEHAVIOR_PROMPTS) + list(probes.IDENTITY_PROMPTS)
    sh = {m: {k: [shingles(x) for x in ans.get(m, {}).get(k, []) if x] for k in bkeys} for m in models}

    def sim(a, b, keys):
        vals = []
        for k in keys:
            xs, ys = sh[a][k], sh[b][k]
            if xs and ys:
                pair = [jaccard(x, y) for x in xs for y in ys]
                vals.append(sum(pair) / len(pair))
        return sum(vals) / len(vals) if vals else None

    def self_sim(m, keys):
        vals = [jaccard(xs[0], xs[1]) for k in keys if len(xs := sh[m][k]) >= 2]
        return sum(vals) / len(vals) if vals else None

    long_keys = ["b_poem", "b_list_tuple", "b_factorial", "b_joke", "b_refusal", "b_markdown"]
    w("Mean 4-gram Jaccard similarity (averaged over all answer pairs) of long-form answers (temperature 0). "
      "`self` = similarity of a model's two repeats with itself, a reference for 'same model' noise.\n")
    pairs = []
    for a, b in combinations(models, 2):
        s = sim(a, b, long_keys)
        if s is not None:
            pairs.append((s, a, b))
    pairs.sort(reverse=True)
    selfs = [s for m in models if (s := self_sim(m, long_keys)) is not None]
    if selfs:
        w(f"- Self-similarity across repeats: mean {sum(selfs)/len(selfs):.3f}, min {min(selfs):.3f}, max {max(selfs):.3f}")
    if pairs:
        vals = [p[0] for p in pairs]
        w(f"- Cross-name similarity: mean {sum(vals)/len(vals):.3f}, min {min(vals):.3f}, max {max(vals):.3f}\n")
        w("Top 15 most similar pairs:\n")
        for s, a, b in pairs[:15]:
            w(f"- {s:.3f}  {a} ↔ {b}")
        w("\nBottom 10 least similar pairs:\n")
        for s, a, b in pairs[-10:]:
            w(f"- {s:.3f}  {a} ↔ {b}")
    w("")

    w("### Short answers per model (first answer)\n")
    sk = ["b_math", "b_strawberry", "b_random", "b_color", "b_name", "b_word"]
    w("| model | " + " | ".join(sk) + " |")
    w("|---" * (len(sk) + 1) + "|")
    for m in models:
        first = lambda k: next((norm(x)[:30] for x in ans.get(m, {}).get(k, []) if x), "")
        w(f"| {m} | " + " | ".join(first(k) for k in sk) + " |")
    w("")
    w("### Short-answer distributions\n")
    for k in ["b_math", "b_strawberry", "b_random", "b_color", "b_name", "b_word", "id_cutoff", "id_context", "id_system"]:
        c = Counter(norm(x)[:40] for m in models for x in ans.get(m, {}).get(k, []) if x)
        w(f"- **{k}**: " + ", ".join(f"`{v}`×{n}" for v, n in c.most_common(8)))
    w("")

    # 4. Metadata
    w("## 4. Operational metadata\n")
    w("| model | ok | err | empty answers | median latency s | reasoning share | response.model |")
    w("|---|---|---|---|---|---|---|")
    for m in models:
        d = met[m]
        lat = sorted(d["lat"])
        med = f"{lat[len(lat)//2]:.1f}" if lat else ""
        rr = f"{sum(d['reason_ratio'])/len(d['reason_ratio']):.2f}" if d["reason_ratio"] else ""
        w(f"| {m} | {d['ok']} | {d['err']} | {d['empty']} | {med} | {rr} | {', '.join(map(str, d['resp_model']))} |")
    w("")
    errs = Counter()
    for m in models:
        errs.update(met[m]["errors"])
    if errs:
        w("Errors seen (after retries):\n")
        for e, n in errs.most_common(10):
            w(f"- {n}× `{e}`")
    w("")

    out = RESULTS / "report.md"
    out.write_text("\n".join(L))
    print(out.read_text())


if __name__ == "__main__":
    main()
