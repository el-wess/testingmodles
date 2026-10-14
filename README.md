# testingmodles: does one API serve the same model under many names?

This project probes an OpenAI-compatible endpoint (`https://radoxai.com/v1`) and
fingerprints each advertised model name. The goal is to check whether the
provider serves one underlying model under 33 different names.

## Verdict

**All 33 model names behave like the same underlying model, very likely from
Meta's Muse family (Muse Spark or its open-weight distillation, Muse Glimmer).**
The provider gives each name a different persona through a hidden system prompt. The
evidence comes from 1,650+ requests (October 14, 2026); full data is in `results/`.

| Signal | What we found |
|---|---|
| **Tokenizer** (strongest) | All 33 names produce **identical** prompt-token counts on 13 probe strings (English, code, Chinese, Japanese, Russian, Arabic, emoji, digits, whitespace, rare words, glitch tokens, hex, repetition). Real tokenizers disagree sharply on these strings. For example, real Gemma-2 and Qwen3 split the 61-digit string into 60 tokens, but every name here, including "gemma-2-2b", counts 20. The shared vector **matches Meta's Muse tokenizer exactly (13/13, via the open-weight Muse Glimmer 30B, which is distilled from Muse Spark)**. Every other public tokenizer we tested matches at most 8 of 13 (OpenAI cl100k/o200k, gpt-oss, Gemma-2, DeepSeek-V3, Qwen3, GLM-4.5, Llama-3.3, Mistral, MiniMax-M2, Kimi-K2). See `results/tokenizer_match.txt`. |
| **Meta leaks** | Three Claude personas slipped and named Meta in Chinese (`我是 Meta 开发的 Claude Opus 4.6 模型。` from claude-opus-4.6, plus claude-mythos-preview and claude-opus-4.7). A GPT persona (gpt-5.6-luna) named its base family `Llama`. No persona leaked any other vendor. |
| **Hidden system prompt** | A one-word prompt costs 285–308 prompt tokens on every name. A hidden system prompt of about 285 tokens is injected, and its length varies slightly by name, which fits a per-name persona template. Models refuse to reveal it, and all of them refuse with nearly the same wording. |
| **Self-identity** | Every name answers "who are you" with the same sentence template (`I am X created and trained by Y.` / `我是 Y 开发的 X 模型。`). Only X and Y change: Claude, GPT, Gemini, Grok, Qwen, DeepSeek, Kimi, GLM, Seed, Muse, Gemma. Every name gives a **January 2026** training cutoff, including "gemma-2-2b", a 2024 model. |
| **Reasoning** | Every name, including "gemma-2-2b" (a non-reasoning 2B model), spends about 87–90% of completion tokens on hidden reasoning. Every name rejects `logprobs` with the same error: "`logprobs` is not supported with reasoning". |
| **Behavioural quirks** | At temperature 0, almost all 66 answers per prompt agree across names: `187×293` → `54791` (63/63 successful answers), `r`s in "strawberrry" → `4`, a colour → `blue` (63×), tavern name → "The Gilded Griffin" (54×). Random-number and "unexpected word" picks come from the same tiny set: 42/73/47; syzygy/defenestration/petrichor. |
| **Long-form similarity** | The mean 4-gram Jaccard similarity *between different names* (0.47) is about the same as the similarity of *one name with its own repeat* (0.49). Different names are as similar as the same name sampled twice. |

### Caveats

- The tokenizer cannot tell Muse Spark (API-only) apart from Muse Glimmer 30B
  (open-weight and free to self-host). Both use the same tokenizer, so the
  backend could be either one, or a specific Spark version (1.1/1.2/1.3).

- The tokenizer test shows that all names share **one tokenizer**. Together with
  the identical quirks and templates, this is strong evidence for one model. It
  cannot strictly rule out several checkpoints or sizes of the *same* family
  behind one tokenizer. It does rule out the advertised mix of vendors, which
  use different tokenizers.
- We had no access to the official vendor APIs, so there is no external
  "known-different" control for the text-similarity metric. The tokenizer and
  quirk signals do not depend on such a control.
- About 50% of requests first got `The backend is temporarily overloaded` and
  were retried with backoff. 58 of 1,650 still failed. The report counts them,
  and the tokenizer comparison uses the probes that succeeded.
- A cross-model prompt-cache test was tried and dropped. The backend did not
  report cache hits for user content even when the same model got the same
  prompt twice, so the test was inconclusive.

## Layout

```
model_probe/
  client.py           OpenAI-compatible client, retry/backoff, logs every request to results/raw*.jsonl
  probes.py           tokenizer strings, identity prompts, behavioural prompts
  run.py              collector (phases: tokenizer, identity, behavior)
  analyze.py          builds results/report.md (tokenizer groups, identities, similarity, metadata)
  tokenizer_match.py  compares the observed token counts against real public tokenizers
results/
  raw*.jsonl          every request/response (no credentials)
  report.md           generated analysis
  tokenizer_match.txt output of tokenizer_match.py
```

## Reproduce

```bash
uv venv && uv pip install requests            # + tiktoken tokenizers huggingface_hub regex for tokenizer_match
cp .env.example .env                           # put your key in RADOX_API_KEY (never commit .env)
set -a; . ./.env; set +a
python -m model_probe.run --workers 20         # ~1,650 requests; takes about an hour because of backend overload
python -m model_probe.analyze                  # writes results/report.md
python -m model_probe.tokenizer_match
```

Phases can run separately or in parallel into separate logs, for example
`--phases behavior --log raw_behavior.jsonl`. `analyze` reads every
`results/raw*.jsonl` file.
