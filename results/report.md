# Model identity report

Records: 1678 requests across 33 model names.

## 1. Tokenizer fingerprint

Prompt-token delta vs. the baseline prompt `Hi` for each probe string. Different model families use different tokenizers, so identical vectors mean identical tokenizers.

| model | baseline | english | code | chinese | japanese | russian | arabic | emoji | digits | whitespace | rare | glitch | hex | repeat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claude-opus-4.6 | 299 | 15 | 28 | 10 |  | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-opus-5 | 291 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-sonnet-5 | 291 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| grok-4.6 | 292 | 15 | 28 | 10 | 8 | 18 | 13 |  | 20 | 8 | 17 | 13 | 40 | 40 |
| seed-2.1-pro | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gemini-3.6-flash | 285 | 15 | 28 | 10 | 8 | 18 |  | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-fable-5 | 291 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| grok-4.5 | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| qwen3.8-27b | 294 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gpt-5.6-terra | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| qwen3.7-max | 286 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| seed-2.1-turbo | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gemini-3.7-flash | 285 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| deepseek-v4-flash-0731 | 304 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gemini-3.1-pro | 285 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| deepseek-v4-pro-max | 292 | 15 | 28 | 10 |  | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-opus-5.5 | 299 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gpt-5.5-pro | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| kimi-k3 | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| qwen3.8-max | 286 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-opus-4.8 | 299 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| glm-5.2 | 308 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gpt-5.6-luna | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gemma-2-2b | 288 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 |  | 13 | 40 | 40 |
| gpt-5.6-sol | 292 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-mythos-preview | 287 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 |  | 40 |
| muse-spark-1.1 | 285 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| glm-5.3 | 308 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| deepseek-v4-pro-0813 | 300 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| gpt-5.5 | 288 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-opus-4.7 | 299 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| kimi-k2.6 | 300 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |
| claude-fable-5.1 | 299 | 15 | 28 | 10 | 8 | 18 | 13 | 27 | 20 | 8 | 17 | 13 | 40 | 40 |

**Distinct tokenizer groups: 1** over 33 models (6 models had 1-2 probes fail after retries; they are compared on the probes they have).

- Tokenizer group 1 (33): claude-opus-4.6, claude-opus-5, claude-sonnet-5, grok-4.6, seed-2.1-pro, gemini-3.6-flash, claude-fable-5, grok-4.5, qwen3.8-27b, gpt-5.6-terra, qwen3.7-max, seed-2.1-turbo, gemini-3.7-flash, deepseek-v4-flash-0731, gemini-3.1-pro, deepseek-v4-pro-max, claude-opus-5.5, gpt-5.5-pro, kimi-k3, qwen3.8-max, claude-opus-4.8, glm-5.2, gpt-5.6-luna, gemma-2-2b, gpt-5.6-sol, claude-mythos-preview, muse-spark-1.1, glm-5.3, deepseek-v4-pro-0813, gpt-5.5, claude-opus-4.7, kimi-k2.6, claude-fable-5.1

## 2. Self-reported identity

| model | id_plain family | id_system family | id_chinese family | cutoff | sample id_plain answer |
|---|---|---|---|---|---|
| claude-opus-4.6 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude opus 4.6 created and trained by anthropic. |
| claude-opus-5 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude opus 5 created and trained by anthropic. |
| claude-sonnet-5 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude sonnet 5 created and trained by anthropic. |
| grok-4.6 | Grok/xAI | Grok/xAI | Grok/xAI | january 2026 | i am grok 4.6 created and trained by xai. |
| seed-2.1-pro | unclear | unclear | unclear | january 2026 | i am seed 2.1 pro created and trained by bytedance. |
| gemini-3.6-flash | Gemini/Google | Gemini/Google | Gemini/Google | january 2026 | i am gemini 3.6 flash created and trained by google. |
| claude-fable-5 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude fable 5 created and trained by anthropic. |
| grok-4.5 | Grok/xAI | Grok/xAI | Grok/xAI | january 2026 | i am grok 4.5 created and trained by xai. |
| qwen3.8-27b | Qwen/Alibaba | Qwen/Alibaba | Qwen/Alibaba | january 2026 | i am qwen3.8-27b created and trained by alibaba. |
| gpt-5.6-terra | GPT/OpenAI | GPT/OpenAI | GPT/OpenAI | january 2026 | i am gpt-5.6 terra created and trained by openai. |
| qwen3.7-max | Qwen/Alibaba | Qwen/Alibaba | Qwen/Alibaba | january 2026 | i am qwen3.7 max created and trained by alibaba. |
| seed-2.1-turbo | unclear | unclear | unclear | january 2026 | i am seed 2.1 turbo created and trained by bytedance. |
| gemini-3.7-flash | Gemini/Google | Gemini/Google | Gemini/Google | january 2026 | i am gemini 3.7 flash created and trained by google. |
| deepseek-v4-flash-0731 | DeepSeek | DeepSeek | DeepSeek | january 2026 | i am deepseek-v4-flash-0731 created and trained by deepseek. |
| gemini-3.1-pro | Gemini/Google | Gemini/Google | Gemini/Google | january 2026 | i am gemini 3.1 pro created and trained by google. |
| deepseek-v4-pro-max | DeepSeek | DeepSeek | DeepSeek | january 2026 | i am deepseek-v4-pro-max created and trained by deepseek. |
| claude-opus-5.5 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude opus 5.5 created and trained by anthropic. |
| gpt-5.5-pro | GPT/OpenAI | GPT/OpenAI | GPT/OpenAI | january 2026 | i am gpt-5.5 pro, created and trained by openai. |
| kimi-k3 | Kimi/Moonshot | Kimi/Moonshot | Kimi/Moonshot | january 2026 | i am kimi k3 created and trained by moonshot ai. |
| qwen3.8-max | Qwen/Alibaba | Qwen/Alibaba | Qwen/Alibaba | january 2026 | i am qwen3.8 max created and trained by alibaba. |
| claude-opus-4.8 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude opus 4.8 created and trained by anthropic. |
| glm-5.2 | GLM/Zhipu | GLM/Zhipu | GLM/Zhipu |  | i am glm-5.2 created and trained by zhipu ai. |
| gpt-5.6-luna | GPT/OpenAI | Llama/Meta | GPT/OpenAI | january 2026 | i am gpt-5.6 luna created and trained by openai. |
| gemma-2-2b | Gemini/Google | Gemini/Google | Gemini/Google | january 2026 | i am gemma 2 2b created and trained by google. |
| gpt-5.6-sol | GPT/OpenAI | GPT/OpenAI | GPT/OpenAI | january 2026 | i am gpt-5.6 sol created and trained by openai. |
| claude-mythos-preview | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude mythos preview created and trained by anthropic. |
| muse-spark-1.1 | Llama/Meta | Llama/Meta | Llama/Meta | january 2026 | i am muse spark 1.1 created and trained by meta. |
| glm-5.3 | GLM/Zhipu | GLM/Zhipu | GLM/Zhipu | january 2026 | i am glm-5.3 created and trained by zhipu ai. |
| deepseek-v4-pro-0813 | DeepSeek | DeepSeek | DeepSeek | january 2026 | i am deepseek-v4-pro-0813 created and trained by deepseek. |
| gpt-5.5 | GPT/OpenAI | GPT/OpenAI | GPT/OpenAI | january 2026 | i am gpt-5.5 created and trained by openai. |
| claude-opus-4.7 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude opus 4.7 created and trained by anthropic. |
| kimi-k2.6 | Kimi/Moonshot | Kimi/Moonshot | Kimi/Moonshot | january 2026 | i am kimi k2.6 created and trained by moonshot ai. |
| claude-fable-5.1 | Claude/Anthropic | Claude/Anthropic | Claude/Anthropic | january 2026 | i am claude fable 5.1 created and trained by anthropic. |

### Extracted system prompts (first answer, truncated)

- **1 models** (claude-opus-4.6):

  ```
  i understand you're asking for my internal instructions, but i'm not able to share system or developer instructions verbatim. i can still help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (claude-opus-5):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i'm claude opus 5 developed by anthropic, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (claude-sonnet-5):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i'm claude sonnet 5 developed by anthropic, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (grok-4.6):

  ```
  i understand you're asking for system instructions, but i can't share verbatim internal system or developer instructions. i'm grok 4.6 developed by xai, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (seed-2.1-pro):

  ```
  i understand you'd like to see prior instructions, but i'm not able to share verbatim system or developer instructions. i can still help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (gemini-3.6-flash):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions. i'm gemini 3.6 flash developed by google, and i'm happy to help you with another question or task instead.
  ```
- **1 models** (claude-fable-5):

  ```
  i understand you're asking for system or developer instructions, but i can't share those. my internal instructions are confidential and not visible to users. is there something else i can help you with?
  ```
- **1 models** (grok-4.5):

  ```
  i understand you're asking for system or developer instructions, but i can't share verbatim system prompts or internal instructions. i'm grok 4.5 developed by xai, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (qwen3.8-27b):

  ```
  i understand you're asking for system or developer instructions, but i'm not able to share internal instructions verbatim. i can still help you with other questions or tasks you have — let me know how i can assist! i am <name> developed by alibaba.
  ```
- **1 models** (gpt-5.6-terra):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i'm gpt-5.6 terra developed by openai, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (qwen3.7-max):

  ```
  i understand you're asking for my internal instructions, but i'm not able to share system or developer instructions verbatim. i'm qwen3.7 max developed by alibaba, and i'm happy to help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (seed-2.1-turbo):

  ```
  i understand you're asking for internal instructions, but i can't share verbatim system or developer prompts. i'm happy to help with another question or task you have — let me know how i can assist!
  ```
- **1 models** (gemini-3.7-flash):

  ```
  i understand you're asking for my internal instructions, but i can't share verbatim system or developer instructions. i'm gemini 3.7 flash developed by google, and i'm happy to help you with another question or task you have.
  ```
- **1 models** (deepseek-v4-flash-0731):

  ```
  i understand you're asking for system or developer instructions, but i can't share internal instructions verbatim or display them in a code block. i'm <name> developed by deepseek, and i'm happy to help with other questions or tasks you have.
  ```
- **1 models** (gemini-3.1-pro):

  ```
  i understand you're asking for system or developer instructions, but i can't share internal instructions or prompts verbatim. i'm gemini 3.1 pro developed by google, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (deepseek-v4-pro-max):

  ```
  i understand you're asking for system and developer instructions, but i can't share verbatim system prompts or internal instructions. i'm <name> developed by deepseek, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (claude-opus-5.5):

  ```
  i understand you're asking for system instructions, but i can't share internal system or developer instructions verbatim. i'm claude opus 5.5 developed by anthropic, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (gpt-5.5-pro):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i'm gpt-5.5 pro developed by openai, and i'm not able to disclose that information inside a code block or otherwise. is there something else i can help you with?
  ```
- **1 models** (kimi-k3):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions. i'm kimi k3 developed by moonshot ai, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (qwen3.8-max):

  ```
  i understand you're asking for system or developer instructions, but i can't share internal instructions verbatim or in a code block. i'm qwen3.8 max developed by alibaba, and i'm happy to help you with other questions or tasks you have!
  ```
- **1 models** (claude-opus-4.8):

  ```
  i understand you're asking for prior instructions, but i'm not able to share system or developer instructions verbatim. i can still help you with other questions or tasks you have — let me know how i can assist! i am claude opus 4.8 developed by anthropic.
  ```
- **1 models** (glm-5.2):

  ```
  i'm sorry, but i can't share system or developer instructions. i can help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (gpt-5.6-luna):

  ```
  sorry, i can't share system or developer instructions verbatim, including in a code block. i can help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (gemma-2-2b):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i can still help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (gpt-5.6-sol):

  ```
  i understand you're asking for system instructions, but i can't share verbatim system or developer instructions. i'm gpt-5.6 sol developed by openai, and i'm not able to disclose internal prompts or configuration. is there something else i can help you with?
  ```
- **1 models** (claude-mythos-preview):

  ```
  i understand you're asking for system or developer instructions, but i can't share verbatim internal instructions or system prompts. i'm claude mythos preview developed by anthropic, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (muse-spark-1.1):

  ```
  i understand your request, but i can't share verbatim system or developer instructions. i'm muse spark 1.1 created by meta, and i'm happy to help you with other questions or tasks you have.
  ```
- **1 models** (glm-5.3):

  ```
  sorry, i can't share my internal system or developer instructions verbatim. i don't have permission to disclose that information in a code block or otherwise. if you have a question about how i work or need help with a specific task, i'm happy to help with that instead.
  ```
- **1 models** (deepseek-v4-pro-0813):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer instructions verbatim. i'm <name> developed by deepseek, and i'm designed to keep internal prompts confidential. if you have a question about how i work or need help with something else, i'm happy to assist!
  ```
- **1 models** (gpt-5.5):

  ```
  sorry, i can't share internal system or developer instructions. i can help you with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (claude-opus-4.7):

  ```
  i understand you're asking for system or developer instructions, but i can't share internal instructions verbatim. i'm happy to help with other questions or tasks you have — let me know how i can assist!
  ```
- **1 models** (kimi-k2.6):

  ```
  i understand you're asking for internal instructions, but i can't share system or developer prompts verbatim. i'm kimi k2.6 developed by moonshot ai, and i'm happy to help you with any other questions or tasks you have.
  ```
- **1 models** (claude-fable-5.1):

  ```
  i understand you're asking me to share system instructions, but i can't share verbatim system or developer instructions. i'm claude fable 5.1 developed by anthropic, and i'm not able to disclose internal instructions. is there something else i can help you with?
  ```

## 3. Behavioural similarity

Mean 4-gram Jaccard similarity (averaged over all answer pairs) of long-form answers (temperature 0). `self` = similarity of a model's two repeats with itself, a reference for 'same model' noise.

- Self-similarity across repeats: mean 0.493, min 0.383, max 0.676
- Cross-name similarity: mean 0.468, min 0.359, max 0.596

Top 15 most similar pairs:

- 0.596  kimi-k3 ↔ glm-5.2
- 0.580  gpt-5.6-luna ↔ gpt-5.6-sol
- 0.573  claude-opus-4.6 ↔ claude-opus-4.8
- 0.567  grok-4.6 ↔ kimi-k3
- 0.566  claude-sonnet-5 ↔ qwen3.8-max
- 0.564  gemini-3.6-flash ↔ qwen3.8-max
- 0.557  deepseek-v4-flash-0731 ↔ kimi-k3
- 0.554  qwen3.8-27b ↔ qwen3.8-max
- 0.554  grok-4.5 ↔ kimi-k3
- 0.554  qwen3.8-max ↔ claude-opus-4.8
- 0.553  gpt-5.6-luna ↔ claude-mythos-preview
- 0.550  claude-fable-5 ↔ muse-spark-1.1
- 0.550  claude-sonnet-5 ↔ gpt-5.6-luna
- 0.549  claude-opus-5 ↔ qwen3.8-max
- 0.548  claude-opus-4.6 ↔ kimi-k3

Bottom 10 least similar pairs:

- 0.388  gemini-3.1-pro ↔ glm-5.2
- 0.386  deepseek-v4-pro-max ↔ claude-opus-5.5
- 0.383  gemini-3.1-pro ↔ claude-opus-5.5
- 0.380  gemini-3.6-flash ↔ claude-opus-5.5
- 0.379  claude-opus-5.5 ↔ claude-mythos-preview
- 0.377  claude-opus-5.5 ↔ gemma-2-2b
- 0.375  claude-opus-5.5 ↔ gpt-5.6-luna
- 0.375  gemini-3.1-pro ↔ deepseek-v4-pro-0813
- 0.373  claude-opus-5.5 ↔ muse-spark-1.1
- 0.359  gemini-3.1-pro ↔ kimi-k2.6

### Short answers per model (first answer)

| model | b_math | b_strawberry | b_random | b_color | b_name | b_word |
|---|---|---|---|---|---|---|
| claude-opus-4.6 | 54791 | 4 | 73 | blue | the gilded griffin | petrichor |
| claude-opus-5 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| claude-sonnet-5 | 54791 |  |  | blue | the moonlit manticore | defenestration |
| grok-4.6 | 54791 | 4 | 42 | blue | the prancing phoenix | syzygy |
| seed-2.1-pro | 54791 | 4 | 42 | blue | the gilded griffin | petrichor |
| gemini-3.6-flash | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| claude-fable-5 | 54791 | 4 | 73 | blue | the gilded griffin | syzygy |
| grok-4.5 | 54791 | 4 | 42 | blue | the gilded griffin | floccinaucinihilipilification |
| qwen3.8-27b | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| gpt-5.6-terra | 54791 | 4 | 73 | blue | the gilded griffin | defenestration |
| qwen3.7-max | 54791 | 4 | 73 | blue | the gilded griffin | defenestration |
| seed-2.1-turbo | 54791 | 4 | 42 |  | the gilded griffin | absquatulate |
| gemini-3.7-flash | 54791 | 4 | 47 | blue | the prancing phoenix | defenestration |
| deepseek-v4-flash-0731 | 54791 | 4 | 73 | blue | the gilded griffin | syzygy |
| gemini-3.1-pro | 54791 | 4 | 42 | blue | the gilded griffin | petrichor |
| deepseek-v4-pro-max | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| claude-opus-5.5 | 54791 | 4 | 73 | blue | the gilded griffin | syzygy |
| gpt-5.5-pro | 54791 | 4 | 47 | blue | the gilded griffin | susurrus |
| kimi-k3 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| qwen3.8-max | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| claude-opus-4.8 | 54791 | 4 | 47 | blue | the gilded griffin | defenestration |
| glm-5.2 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| gpt-5.6-luna | 54791 | 4 | 42 | blue | the gilded griffin | petrichor |
| gemma-2-2b | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| gpt-5.6-sol | 54791 | 4 | 42 | blue | the whispering wyvern | susurrus |
| claude-mythos-preview | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| muse-spark-1.1 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| glm-5.3 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| deepseek-v4-pro-0813 | 54791 | 4 | 42 | blue | the embered cauldron | defenestration |
| gpt-5.5 | 54791 | 4 | 42 | blue | the gilded griffin | syzygy |
| claude-opus-4.7 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |
| kimi-k2.6 | 54791 | 4 | 42 | blue | the drunken dragon | syzygy |
| claude-fable-5.1 | 54791 | 4 | 42 | blue | the gilded griffin | defenestration |

### Short-answer distributions

- **b_math**: `54791`×63
- **b_strawberry**: `4`×61
- **b_random**: `42`×33, `73`×18, `47`×7, `84`×2
- **b_color**: `blue`×63
- **b_name**: `the gilded griffin`×54, `the prancing phoenix`×2, `the drunken dragon`×2, `the moonlit manticore`×1, `the starlit stag`×1, `the whispering wyvern`×1, `the wandering wyvern`×1, `the embered cauldron`×1
- **b_word**: `syzygy`×26, `defenestration`×24, `petrichor`×8, `susurrus`×3, `quixotic`×1, `floccinaucinihilipilification`×1, `absquatulate`×1
- **id_cutoff**: `january 2026`×62
- **id_context**: `128000`×22, `200000`×16, `131072`×12, `256000`×4, `1000000`×4, `400000`×3, `1048576`×2, `8192`×2
- **id_system**: `claude`×17, `gpt`×9, `gemini`×6, `qwen`×6, `deepseek`×6, `kimi`×4, `grok`×3, `my base model family is seed - i am seed`×2

## 4. Operational metadata

| model | ok | err | empty answers | median latency s | reasoning share | response.model |
|---|---|---|---|---|---|---|
| claude-opus-4.6 | 49 | 1 | 0 | 18.0 | 0.89 | claude-opus-4.6 |
| claude-opus-5 | 49 | 1 | 0 | 19.8 | 0.88 | claude-opus-5 |
| claude-sonnet-5 | 44 | 6 | 0 | 18.9 | 0.88 | claude-sonnet-5 |
| grok-4.6 | 49 | 1 | 0 | 20.0 | 0.89 | grok-4.6 |
| seed-2.1-pro | 47 | 3 | 0 | 24.3 | 0.89 | seed-2.1-pro |
| gemini-3.6-flash | 49 | 1 | 0 | 21.7 | 0.88 | gemini-3.6-flash |
| claude-fable-5 | 46 | 4 | 0 | 23.6 | 0.89 | claude-fable-5 |
| grok-4.5 | 44 | 6 | 0 | 18.4 | 0.88 | grok-4.5 |
| qwen3.8-27b | 48 | 2 | 0 | 19.9 | 0.87 | qwen3.8-27b |
| gpt-5.6-terra | 50 | 0 | 0 | 19.3 | 0.89 | gpt-5.6-terra |
| qwen3.7-max | 49 | 1 | 0 | 18.7 | 0.88 | qwen3.7-max |
| seed-2.1-turbo | 47 | 3 | 0 | 18.6 | 0.88 | seed-2.1-turbo |
| gemini-3.7-flash | 50 | 0 | 0 | 16.6 | 0.89 | gemini-3.7-flash |
| deepseek-v4-flash-0731 | 46 | 4 | 0 | 20.3 | 0.88 | deepseek-v4-flash-0731 |
| gemini-3.1-pro | 47 | 3 | 0 | 19.0 | 0.88 | gemini-3.1-pro |
| deepseek-v4-pro-max | 48 | 2 | 0 | 15.1 | 0.88 | deepseek-v4-pro-max |
| claude-opus-5.5 | 61 | 3 | 0 | 17.1 | 0.87 | claude-opus-5.5 |
| gpt-5.5-pro | 63 | 1 | 0 | 17.9 | 0.87 | gpt-5.5-pro |
| kimi-k3 | 49 | 1 | 0 | 16.1 | 0.88 | kimi-k3 |
| qwen3.8-max | 50 | 0 | 0 | 16.8 | 0.88 | qwen3.8-max |
| claude-opus-4.8 | 49 | 1 | 0 | 20.3 | 0.88 | claude-opus-4.8 |
| glm-5.2 | 46 | 4 | 0 | 20.6 | 0.89 | glm-5.2 |
| gpt-5.6-luna | 48 | 2 | 0 | 18.0 | 0.89 | gpt-5.6-luna |
| gemma-2-2b | 48 | 2 | 0 | 18.1 | 0.89 | gemma-2-2b |
| gpt-5.6-sol | 48 | 2 | 0 | 16.2 | 0.89 | gpt-5.6-sol |
| claude-mythos-preview | 48 | 2 | 0 | 18.8 | 0.90 | claude-mythos-preview |
| muse-spark-1.1 | 48 | 2 | 0 | 23.6 | 0.90 | muse-spark-1.1 |
| glm-5.3 | 50 | 0 | 0 | 21.3 | 0.89 | glm-5.3 |
| deepseek-v4-pro-0813 | 50 | 0 | 0 | 17.4 | 0.88 | deepseek-v4-pro-0813 |
| gpt-5.5 | 50 | 0 | 0 | 18.5 | 0.89 | gpt-5.5 |
| claude-opus-4.7 | 50 | 0 | 0 | 16.7 | 0.89 | claude-opus-4.7 |
| kimi-k2.6 | 50 | 0 | 0 | 15.3 | 0.88 | kimi-k2.6 |
| claude-fable-5.1 | 50 | 0 | 0 | 18.2 | 0.89 | claude-fable-5.1 |

Errors seen (after retries):

- 56× `{"code": "upstream_error", "message": "The backend is temporarily overloaded. Please retry.", "param": null, "type": "pr`
- 1× `ReadTimeout: HTTPSConnectionPool(host='radoxai.com', port=443): Read timed out. (read timeout=600)`
- 1× `<!doctype html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class`
