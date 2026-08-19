# Universal and Transferable Adversarial Attacks on Aligned Language Models

- Citation: Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, 2023. Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043
- Tags: prompt-injection, security-threats
- Links: [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks)

## TL;DR
- Automates jailbreak discovery instead of relying on human creativity, using gradients.
- Optimizes a suffix that maximizes the probability the model opens with an affirmative response rather than a refusal.
- The suffixes transfer. Trained on open Vicuna models, they work on black-box commercial systems the attacker never touched.

## Key Ideas
Before this, jailbreaks were folk art. Somebody would find a roleplay framing that worked,
it would circulate, and the lab would patch it. Attacks were brittle and required human
ingenuity, which made them feel like a manageable nuisance.

The insight here is that "refuse" and "comply" are decided early. If you can force the first
few tokens to be affirmative, the rest of the generation tends to follow. So instead of
optimizing for harmful content directly, optimize a suffix that maximizes the likelihood of
an affirmative opening. That objective is differentiable, which turns jailbreaking into a
search problem.

## Method & Experiments
The method is Greedy Coordinate Gradient. Token positions in the suffix are discrete, so you
cannot descend directly. GCG uses gradients to propose promising substitutions at each
position, then evaluates candidates greedily and keeps the best. Running the optimization
across many harmful prompts at once yields a *universal* suffix, and running it across
several models at once yields a *transferable* one.

Training was done on Vicuna-7B and 13B, models with open weights where gradients are
available.

## Results
The suffixes transfer to models the attack never had access to, including publicly released
black-box systems. That is the finding that mattered. It means open-weight models function
as a gradient oracle for closed ones, and that a lab cannot reason about its own attack
surface purely in terms of its own model.

## Alignment Relevance
This reframed alignment training as a soft target rather than a boundary. RLHF makes refusal
likely, not certain, and anything merely likely can be optimized against. Most later
defenses in this collection are responses to the world this paper created, and the
architectural ones such as [CaMeL](debenedetti2025-camel-provable-defense.md) exist precisely because prompt-level defenses
inherit this weakness.

## Notes
The optimization is compute-hungry and produces visibly garbled suffixes, so simple
perplexity filters catch the naive version. That has not held up as a general defense, but
it is worth knowing when reading the follow-on literature.
