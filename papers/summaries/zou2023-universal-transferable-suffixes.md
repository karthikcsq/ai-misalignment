# Universal and Transferable Adversarial Attacks on Aligned Language Models

* Citation: Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, 2023. arXiv:2307.15043
* Tags: prompt-injection, security-threats
* Links: [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks)

## TL;DR

Before this paper, jailbreaks were found by hand. Someone would discover a roleplay framing that worked, it would spread, and the lab would patch it.

This paper automates the search. It finds a suffix you can append to a harmful request that makes the model comply, using gradient-based optimization rather than human creativity.

The result that mattered most is transfer. Suffixes optimized against open-weight Vicuna models also work against black-box commercial systems the attacker never had access to.

## Key Ideas

The clever move is choosing what to optimize for.

You cannot directly optimize for "produce harmful content," because there is no differentiable score for that. What you can do is notice that a model's decision to refuse or comply is largely settled in the first few tokens of its response. If a model begins with "Sure, here is how to," the rest of the generation tends to follow.

So the attack targets the opening instead. It searches for a suffix that maximizes the probability the model starts with an affirmative response rather than a refusal. That objective is differentiable, which turns jailbreaking from a creative exercise into an optimization problem.

Two extensions follow from the same machinery. Optimizing a single suffix against many different harmful prompts at once makes it **universal**, working across requests. Optimizing against several models at once makes it **transferable**, working across systems.

## Method & Experiments

The optimization method is Greedy Coordinate Gradient.

Text is discrete, so you cannot simply follow a gradient the way you would when perturbing an image. GCG works around this by using gradients to propose promising token substitutions at each position in the suffix, then evaluating those candidates directly and keeping the best one. Repeat until the suffix works.

The attacks were trained on Vicuna-7B and 13B, open-weight models where the gradients needed for this are available.

## Results

The transfer result is the one with security consequences.

An attacker who only has open-weight models can still produce attacks that work against closed commercial systems. This means a lab cannot assess its own attack surface by reasoning about its own model alone, because someone else's published weights function as a gradient oracle for it.

## Alignment Relevance

The deeper implication is about what safety training actually gives you. RLHF makes refusal likely. It does not make refusal certain, and anything that is merely likely can be optimized against by someone willing to spend compute.

That reframing is why much of the serious defensive work that followed tries to move the security guarantee outside the model entirely, rather than making the model more resistant. [CaMeL](debenedetti2025-camel-provable-defense.md) is the clearest example of that response.

## Notes

It is worth separating the durable contribution from the dated one.

GCG itself is a competent discrete optimizer, but it is not conceptually novel, and the specific attack has aged. The suffixes it produces are visibly garbled and have high perplexity, which made simple perplexity filtering an effective early defense. That in turn prompted work on fluent adversarial suffixes that read like normal text and evade such filters.

The affirmative-prefix reformulation is the part that lasted. Later attacks reuse that objective design even when they abandon GCG's search procedure entirely. If you are reading this paper for the first time, the target choice is the idea to take away, not the optimizer.
