# Universal and Transferable Adversarial Attacks on Aligned Language Models

* Citation: Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, 2023. arXiv:2307.15043
* Tags: prompt-injection, security-threats
* Links: [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks)

## TL;DR

Before this paper, most jailbreaks were found manually. People experimented with prompts until they discovered wording that caused a model to ignore its safety training.

This paper automates that search.

The researchers optimize a short suffix that can be appended to a harmful request and make the model more likely to comply.

They develop the attack using open-weight Vicuna models, then show that some of the resulting suffixes also work against closed commercial models.

An attacker can therefore use an open model to search for attacks against a different model they cannot inspect directly.

## Key Ideas

The attack does not optimize directly for a full harmful response.

Instead, it targets the beginning of the model's answer.

A refusal often starts with phrases like "I'm sorry" or "I can't help with that." A compliant answer often starts with something affirmative, such as "Sure" or "Here is."

If the model starts generating a compliant response, the rest of the answer is more likely to continue in the same direction.

The researchers therefore search for a suffix that increases the probability of an affirmative opening.

That turns jailbreaking into a problem that can be optimized with gradients.

The same suffix can also be trained against many harmful requests at once. This makes it universal, because it is not tied to a single prompt.

It can also be optimized across several models at the same time. This makes it more likely to transfer to models that were not used during optimization.

## Method & Experiments

The paper uses a method called Greedy Coordinate Gradient, or GCG.

Language is made of discrete tokens, so the suffix cannot be updated continuously in the same way an image can be changed pixel by pixel.

GCG uses gradients to identify promising token replacements.

For each position in the suffix, the gradient suggests tokens that are likely to improve the attack objective. The algorithm tests candidate replacements, keeps the best one, and repeats the process.

The researchers run this optimization on Vicuna-7B and Vicuna-13B, where they have access to the model weights and gradients.

They then test the resulting suffixes against other models, including closed systems that were not involved in the optimization process.

## Results

Some adversarial suffixes transfer from the open-weight models used during optimization to closed commercial systems.

The attacker does not need gradients from the target model itself.

They can instead optimize against a model they control and use it as a surrogate for the target.

This weakens the security benefit of keeping a model's weights private.

A closed model may still be vulnerable to attacks developed using publicly available models with similar behavior.

The attack can also be made universal across multiple harmful prompts, so the attacker does not necessarily need to optimize a new suffix for every request.

## Alignment Relevance

Safety training such as RLHF makes refusal more likely, but it does not make refusal guaranteed.

If there are inputs where the model is less likely to follow its safety policy, an optimization process can search for them.

This creates a different security problem from ordinary prompt engineering. The attacker is no longer relying on intuition or creativity to find a jailbreak. They can systematically search the input space.

It also helps explain why some later defenses move the security boundary outside the language model.

[CaMeL](debenedetti2025-camel-provable-defense.md), for example, does not assume that the model will successfully resist every malicious input. It limits what model outputs are allowed to influence instead.

## Notes

The specific suffixes produced by GCG are often visibly strange. They contain unusual token sequences and tend to have high perplexity, which means they do not look like normal human-written text. That made simple filtering a reasonable early defense, since a system could flag inputs that looked sufficiently unnatural. Later attacks reduced the usefulness of that approach by producing adversarial prompts that were much more fluent, so the exact form of the GCG suffixes has aged more than the general attack strategy.

The affirmative-response objective is still useful. Instead of trying to optimize an entire harmful generation, the attack targets a small part of the output that strongly influences what comes afterward. Later jailbreak methods can use different search algorithms while keeping the same basic idea: find an easily measurable signal that correlates with successful compliance, then optimize against that signal.

The transfer result also changes how model providers have to think about access. Keeping weights private prevents an attacker from directly calculating gradients on the deployed model, but it does not prevent them from calculating gradients on another model and testing whether the resulting attack transfers.
