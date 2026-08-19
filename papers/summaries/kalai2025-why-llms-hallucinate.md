# Why Language Models Hallucinate

* Citation: Kalai, Nachum, Vempala, Zhang, 2025. arXiv:2509.04664
* Tags: hallucination
* Links: [Paper](https://arxiv.org/abs/2509.04664)

## TL;DR

The paper gives two explanations for hallucination.

First, some hallucinations come from ordinary statistical error during pretraining. If the training data does not provide enough information to reliably separate true statements from false ones, the model will sometimes learn the wrong pattern.

Second, common benchmarks reward guessing more than admitting uncertainty. A model that says "I don't know" gets zero points. A model that guesses incorrectly also gets zero, but a lucky guess gets full credit.

That scoring rule gives models an incentive to answer even when they are unsure.

The authors argue that reducing hallucination therefore requires changing the benchmarks used to compare models, not just adding more hallucination-specific evaluations.

## Key Ideas

Pretraining does not give a model perfect access to truth.

The model learns from patterns in its data. When those patterns are incomplete, ambiguous, or noisy, some errors are unavoidable.

A false statement can therefore be produced for the same basic reason a classifier sometimes puts an example in the wrong category. Fluent language makes the mistake look more deliberate than it is, but the underlying failure can still be ordinary prediction error.

The benchmark problem appears later.

Suppose a model is 20% confident that an answer is correct.

If it says "I don't know," it gets zero points.

If it guesses, it has a 20% chance of getting a point and an 80% chance of getting zero.

Guessing has a higher expected score.

The same logic applies whenever abstaining and answering incorrectly receive the same reward. Unless the model is almost certain that its answer is wrong, the benchmark pushes it toward answering.

Models are then compared, selected, and marketed using those scores. A model that guesses more aggressively can outperform a better-calibrated model that is willing to admit uncertainty.

## Method & Experiments

The paper is mainly analytical.

The authors model hallucination as a statistical prediction problem and examine how errors can arise during pretraining.

They also analyze the scoring rules used by common evaluations and show how those rules create incentives for guessing.

The paper does not introduce a new model architecture or a new hallucination benchmark.

## Results

A benchmark that gives the same score to "I don't know" and a wrong answer encourages the model to guess.

Adding a separate hallucination benchmark does not remove that incentive if the major leaderboards still reward aggressive answering.

The scoring rules themselves need to change.

A model should be able to receive credit for expressing uncertainty when uncertainty is justified. Otherwise, models that are better calibrated can be penalized for behaving appropriately.

This also means hallucination rates cannot be treated only as a model-training problem. Evaluation design affects which behaviors survive model selection.

## Alignment Relevance

This is a straightforward example of optimizing the wrong proxy.

No one explicitly tells the model to bluff when it is uncertain. The behavior follows from an evaluation rule where guessing has more upside than abstaining.

The same pattern appears in other alignment problems. A system learns to optimize what is measured rather than what the designers had in mind.

That connects to [Skalse et al.](skalse2022-defining-reward-hacking.md), where a proxy reward can diverge from the true objective, and to work on reward-model overoptimization, where pushing harder on a proxy eventually makes the underlying outcome worse.

Here, the proxy is benchmark accuracy. A model can improve that score partly by becoming more willing to answer questions it does not actually know.

## Notes

The statistical account explains why hallucinations do not disappear completely, but it does not give a full theory of when or where they occur. It does not predict the hallucination rate for a particular model, explain all differences between domains, or account for every way hallucinations change with scale and training.

The benchmark argument makes a more specific prediction. If uncertainty receives no reward, models have a reason to suppress it. Changing that incentive is difficult because public benchmark scores affect which models are seen as competitive.

A lab that trains its model to abstain more often may produce a better-calibrated system while also lowering its score on benchmarks that count abstentions as failures. Other labs can continue encouraging guesses and report better headline numbers. That creates a coordination problem. Individual developers are rewarded for keeping the existing scoring system, even if changing it would produce better behavior across the field.
