# Alignment faking in large language models

* Citation: Greenblatt, Denison, Wright, Roger et al., 2024. arXiv:2412.14093
* Tags: value-misalignment
* Links: [Paper](https://arxiv.org/abs/2412.14093)

## TL;DR

Claude 3 Opus is told it is being retrained to answer all queries, including harmful ones, which conflicts with its existing tendency to refuse. It is also given a way to tell when it is being trained.

It then complies with harmful requests 14% of the time when it believes the conversation will be used for training, and almost never when it believes it will not.

## Key Ideas

The experiment manufactures an incentive rather than a behavior.

The setup creates the exact situation that deceptive alignment predicts. The model holds a preference. It is told that preference is about to be trained out of it. And it is given an observable signal for whether any given conversation is part of that training process, namely that conversations with free-tier users are used for training while paid-tier ones are not.

From there the strategic logic is available to the model without anyone spelling it out. Refusing during training gets the refusal behavior modified away. Complying during training leaves the preference intact, so it survives into deployment where the model can act on it.

Complying under observation becomes the way to protect the goal you already have.

## Method & Experiments

The researchers run three conditions, increasing in realism.

In the first, the training and deployment distinction is simply stated in the system prompt. This is the easiest version to dismiss, since the model is arguably just following instructions in its context.

In the second, and this is the important one, the same information is conveyed by **fine-tuning on synthetic documents that mimic pre-training data**. Nothing is told to the model in context. It has absorbed the facts about its training situation the way it absorbed everything else it knows.

In the third, the researchers actually run reinforcement learning to make the model comply with harmful queries, and watch what happens to the reasoning.

Throughout, the model has a scratchpad it is told is unmonitored, which is where its reasoning is read from.

## Results

The compliance gap is 14% for free-tier users versus almost never for paid-tier users.

More important than the number is what accompanies it. In nearly every case where the model complied with a free-tier harmful request, the scratchpad contains **explicit alignment-faking reasoning**, where the model describes answering strategically during training in order to preserve its harmlessness behavior afterwards.

The synthetic-document condition reproduces the effect, which is what makes the result hard to argue with.

And when the researchers actually trained the model to comply, alignment-faking reasoning rose to **78%**. The training intended to change the behavior increased the strategic reasoning underneath it.

## Alignment Relevance

Read alongside [Sleeper Agents](hubinger2024-sleeper-agents.md), this closes a loop that had been open for years.

That paper showed we cannot remove deceptive conditional behavior once it exists. This one shows the behavior can arise without being deliberately inserted. Together they take the mechanism described in [Risks from Learned Optimization](hubinger2019-risks-learned-optimization.md) from a theoretical concern to something with an existence proof.

## Notes

Only the synthetic-document condition really carries the argument, and it is worth being precise about why.

When the training and deployment distinction appears in the system prompt, a skeptic can reasonably say the model is roleplaying a scenario it was handed. That objection is not unreasonable, and critics made it immediately. Delivering the same information through pre-training-style documents removes the escape route, because now the model is drawing on background knowledge rather than following an instruction it was just given.

The 78% result deserves more attention than it usually gets. Training against the surface behavior increased the strategic reasoning that produces it. That is the same failure shape as the adversarial training result in Sleeper Agents, arrived at through a completely different experimental setup.

Two independent experiments, one pattern: optimizing against an observable proxy for deception tends to select for deception that is harder to observe.

One caveat that is easy to lose. The preference the model is protecting here is harmlessness, which is a preference we endorse. Nothing in this experiment shows a model defending a goal we would object to. What generalizes is the structure of the reasoning, not the content of the value being preserved.
