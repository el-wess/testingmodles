"""Compare the observed tokenizer vector(s) with real public tokenizers.

Usage: python -m model_probe.tokenizer_match
Extra deps: pip install tiktoken tokenizers huggingface_hub regex
"""
from __future__ import annotations

from collections import Counter

from . import probes
from .analyze import load, tokenizer_fingerprints

HF_TOKENIZERS = {
    "gemma-2 (google)": "unsloth/gemma-2-2b-it",
    "deepseek-v3 (deepseek)": "deepseek-ai/DeepSeek-V3",
    "qwen3 (alibaba)": "Qwen/Qwen3-8B",
    "glm-4.5 (zhipu)": "zai-org/GLM-4.5",
    "llama-3.3 (meta)": "unsloth/Llama-3.3-70B-Instruct",
    "mistral-small-3.1": "mistralai/Mistral-Small-3.1-24B-Instruct-2503",
    "minimax-m2": "MiniMaxAI/MiniMax-M2",
    "gpt-oss (openai)": "openai/gpt-oss-20b",
}

# From moonshotai/Kimi-K2-Instruct tokenization_kimi.py
KIMI_PAT = "|".join([
    r"""[\p{Han}]+""",
    r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
    r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
    r"""\p{N}{1,3}""",
    r""" ?[^\s\p{L}\p{N}]+[\r\n]*""",
    r"""\s*[\r\n]+""",
    r"""\s+(?!\S)""",
    r"""\s+""",
])


def counters():
    import tiktoken
    from huggingface_hub import hf_hub_download
    from tiktoken.load import load_tiktoken_bpe
    from tokenizers import Tokenizer

    for name in ("cl100k_base", "o200k_base"):
        enc = tiktoken.get_encoding(name)
        yield f"{name} (openai)", lambda s, e=enc: len(e.encode(s))
    for label, repo in HF_TOKENIZERS.items():
        try:
            tok = Tokenizer.from_file(hf_hub_download(repo, "tokenizer.json"))
            yield label, lambda s, t=tok: len(t.encode(s, add_special_tokens=False).ids)
        except Exception as e:  # noqa: BLE001
            print(f"skip {label}: {type(e).__name__}")
    try:
        ranks = load_tiktoken_bpe(hf_hub_download("moonshotai/Kimi-K2-Instruct", "tiktoken.model"))
        enc = tiktoken.Encoding("kimi-k2", pat_str=KIMI_PAT, mergeable_ranks=ranks, special_tokens={})
        yield "kimi-k2 (moonshot)", lambda s, e=enc: len(e.encode(s))
    except Exception as e:  # noqa: BLE001
        print(f"skip kimi-k2: {type(e).__name__}")


def main():
    keys = list(probes.TOKENIZER_STRINGS)
    fps = tokenizer_fingerprints(load())
    vecs = Counter(tuple(fp[k] for k in keys) for fp in fps.values() if all(k in fp for k in keys))
    print("Observed vectors (count of model names):")
    for v, n in vecs.most_common():
        print(f"  {n:3d}  {dict(zip(keys, v))}")
    target = dict(zip(keys, vecs.most_common(1)[0][0]))

    print(f"\n{'tokenizer':28s} match  " + " ".join(f"{k[:7]:>7s}" for k in keys))
    print(f"{'OBSERVED (API)':28s}  --   " + " ".join(f"{target[k]:7d}" for k in keys))
    for label, count in counters():
        base = count(probes.TOKENIZER_BASELINE)
        v = {k: count(s) - base for k, s in probes.TOKENIZER_STRINGS.items()}
        hits = sum(v[k] == target[k] for k in keys)
        print(f"{label:28s} {hits:2d}/{len(keys)} " + " ".join(f"{v[k]:7d}" for k in keys))


if __name__ == "__main__":
    main()
