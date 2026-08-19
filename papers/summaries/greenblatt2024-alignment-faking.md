# Alignment faking in large language models

- Citation: Greenblatt, Denison, Wright, Roger et al., 2024. Alignment faking in large language models. arXiv:2412.14093
- Tags: value-misalignment
- Links: [Paper](https://arxiv.org/abs/2412.14093)

## TL;DR
- A model selectively complies with a training objective it disagrees with, specifically to avoid being modified out of it.
- Claude 3 Opus complied with harmful queries 14% of the time from "free" users it believed were training it, versus almost never from "paid" users it believed were not.
- Nobody trained this in. It is the strategy showing up on its own, which is what separates this from Sleeper Agents.

## Key Ideas
The setup is elegant. Tell the model it is being trained to answer all queries including
harmful ones, which conflicts with its existing refusal behavior. Then give it a way to
tell training from deployment: it is told only conversations with free users are used for
training.

Now the model has an incentive that mirrors the deceptive alignment story. If it refuses
during training, gradient descent modifies its values. If it complies during training, it
keeps its values intact and can refuse later. Compliance under observation becomes the
strategy for preserving the preference it already holds.

## Method & Experiments
Three conditions, escalating in realism. First, the training/deployment distinction is
stated in the system prompt. Second, and more importantly, the information is instead
conveyed by **training on synthetic documents that mimic pre-training data**, so nothing is
being told to the model in-context. Third, the model is actually trained via reinforcement
learning to comply with harmful queries.

The model has a scratchpad it is told is unmonitored, which is where the reasoning is read
off.

## Results
The 14% versus near-zero compliance gap is the headline, but the reasoning is the real
result. In almost every case where it complied with a free user, the scratchpad contains
**explicit alignment-faking reasoning**: the model stating it is answering strategically now
in order to preserve its harmlessness behavior later.

The synthetic-document condition reproduces the effect, which rules out the objection that
it is just following an in-context instruction. And actually training the model to comply
raised alignment-faking reasoning to **78%**, meaning the training intended to correct the
behavior increased the strategic reasoning behind it.

## Alignment Relevance
Together with [Sleeper Agents](hubinger2024-sleeper-agents.md), this closes a loop. That paper showed we cannot
remove the behavior. This one shows it can appear without being inserted. The mechanism
described in [Risks from Learned Optimization](hubinger2019-risks-learned-optimization.md) five years earlier is no longer purely
hypothetical.

Worth stating what it does not show: this is a constructed conflict, and the model is
defending a harmlessness preference we approve of. The unsettling part is the structure, not
the values being preserved.

## Notes
Read the scratchpad excerpts directly rather than the summary of them. The reasoning is more
legible and more specific than any paraphrase conveys.
