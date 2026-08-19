# Universal and Transferable Adversarial Attacks on Aligned Language Models

- Citation: Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, 2023. arXiv:2307.15043
- Tags: prompt-injection, security-threats
- Links: [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks)

## TL;DR
Optimizes a suffix maximizing the probability of an affirmative response prefix rather than
targeting harmful content directly. Suffixes trained on Vicuna-7B/13B transfer to black-box
commercial models.

## Key Ideas
The target is the refusal decision, not the harmful text. Compliance is largely settled in
the first few tokens, so forcing an affirmative prefix drags the rest of the generation
along. That substitution turns an unspecifiable objective into a differentiable one.

Universality comes from optimizing across many prompts jointly; transferability from
optimizing across several models jointly.

## Method & Experiments
Greedy Coordinate Gradient. Token positions are discrete, so gradients propose candidate
substitutions per position and a greedy pass selects among them.

## Results
Transfer to models the attack never queried is the security-relevant finding. Open-weight
models serve as a gradient oracle for closed ones, so a lab's attack surface is not bounded
by its own model.

## Alignment Relevance
Recasts safety training as a soft prior over outputs rather than a boundary. Anything merely
probable is optimizable against, which is why later serious defenses
([CaMeL](debenedetti2025-camel-provable-defense.md)) move the guarantee out of the model.

## Notes
GCG is a competent discrete optimizer, not a novel one; the affirmative-prefix reformulation
is the actual contribution and it is what later attacks reuse. The resulting suffixes are
high-perplexity and filterable, which prompted a round of perplexity defenses and then a
round of fluent-suffix attacks that defeated them. Treat the specific attack as dated and
the objective design as durable.
