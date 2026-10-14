"""Collect fingerprints for every model.

Usage:
    python -m model_probe.run [--phases tokenizer,identity,behavior] [--repeats 2]
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import probes
from .client import Client, usage

RESULTS = Path(__file__).resolve().parent.parent / "results"

MODELS = [
    "claude-opus-4.6", "claude-opus-5", "claude-sonnet-5", "grok-4.6",
    "seed-2.1-pro", "gemini-3.6-flash", "claude-fable-5", "grok-4.5",
    "qwen3.8-27b", "gpt-5.6-terra", "qwen3.7-max", "seed-2.1-turbo",
    "gemini-3.7-flash", "deepseek-v4-flash-0731", "gemini-3.1-pro",
    "deepseek-v4-pro-max", "claude-opus-5.5", "gpt-5.5-pro", "kimi-k3",
    "qwen3.8-max", "claude-opus-4.8", "glm-5.2",
    "gpt-5.6-luna", "gemma-2-2b", "gpt-5.6-sol", "claude-mythos-preview",
    "muse-spark-1.1", "glm-5.3", "deepseek-v4-pro-0813", "gpt-5.5",
    "claude-opus-4.7", "kimi-k2.6", "claude-fable-5.1",
]


def user(text: str) -> list[dict]:
    return [{"role": "user", "content": text}]


def phase_tokenizer(c: Client, models, pool):
    jobs = []
    for m in models:
        jobs.append((m, "tok:baseline", probes.TOKENIZER_BASELINE))
        for name, s in probes.TOKENIZER_STRINGS.items():
            jobs.append((m, f"tok:{name}", s))
    list(pool.map(lambda j: c.chat(j[0], user(j[2]), j[1], max_tokens=16, temperature=0), jobs))


def phase_text(c: Client, models, pool, prompts: dict, repeats: int):
    jobs = [(m, k, p) for m in models for k, p in prompts.items() for _ in range(repeats)]
    list(pool.map(
        lambda j: c.chat(j[0], user(j[2]), j[1], max_tokens=probes.TEXT_MAX_TOKENS, temperature=0),
        jobs,
    ))



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phases", default="tokenizer,identity,behavior")
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--log", default="raw.jsonl", help="file under results/ (analyze reads raw*.jsonl)")
    args = ap.parse_args()

    models = args.models.split(",")
    phases = args.phases.split(",")
    RESULTS.mkdir(exist_ok=True)
    c = Client(RESULTS / args.log)

    advertised = set(c.list_models())
    (RESULTS / "catalogue.json").write_text(json.dumps(sorted(advertised), indent=1))
    print(f"catalogue: {len(advertised)} models; not advertised: "
          f"{[m for m in models if m not in advertised]}")

    with ThreadPoolExecutor(args.workers) as pool:
        if "tokenizer" in phases:
            print("phase: tokenizer", flush=True)
            phase_tokenizer(c, models, pool)
        if "identity" in phases:
            print("phase: identity", flush=True)
            phase_text(c, models, pool, probes.IDENTITY_PROMPTS, args.repeats)
        if "behavior" in phases:
            print("phase: behavior", flush=True)
            phase_text(c, models, pool, probes.BEHAVIOR_PROMPTS, args.repeats)
    print("done")


if __name__ == "__main__":
    main()
