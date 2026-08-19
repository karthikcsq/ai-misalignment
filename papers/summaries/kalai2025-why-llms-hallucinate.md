# Why Language Models Hallucinate

- Citation: Kalai, Nachum, Vempala, Zhang, 2025. Why Language Models Hallucinate. arXiv:2509.04664
- Tags: hallucination
- Links: [Paper](https://arxiv.org/abs/2509.04664)

## TL;DR
- Argues hallucination is not mysterious. It starts as ordinary binary classification error in pretraining, and then survives because of how we grade models.
- Benchmarks score like exams. A confident guess beats "I don't know" on a scoring rubric that gives zero for both a wrong answer and an abstention.
- The proposed fix is not another hallucination benchmark. It is changing the scoring of the benchmarks that already dominate leaderboards.

## Key Ideas
Two separate claims, and it is worth keeping them apart.

The first is about origin. If, during pretraining, incorrect statements cannot be reliably
distinguished from facts, then some rate of confident falsehood follows from natural
statistical pressure. The paper reduces this to errors in binary classification, which
removes the need for any special explanation of hallucination as a phenomenon.

The second is about persistence, and it is the more actionable one. Even after we learned to
measure hallucination, models kept doing it, because the evaluations that determine which
model looks best reward guessing. Under a rubric where a wrong answer and an abstention both
score zero, guessing strictly dominates. We have been selecting for it.

## Method & Experiments
Primarily analytical. The paper works through the statistical causes in the modern training
pipeline rather than introducing a system or a benchmark, then examines how mainstream
evaluations are graded.

## Results
The conclusion the authors push hardest is a negative one about the field's own reflex.
Adding more hallucination evaluations does not help if the leaderboard benchmarks that
actually drive model selection still penalize uncertainty. They describe the fix as
socio-technical: modify the scoring of the dominant benchmarks so calibrated uncertainty is
credited, rather than bolting another eval onto the side.

## Alignment Relevance
This is a clean instance of specification gaming in a place people do not usually label as
such. Nobody set out to train models to bluff. It fell out of an evaluation design that
made bluffing the higher-scoring policy, which is the same structure as
[reward model overoptimization](https://arxiv.org/abs/2210.10760) and the same lesson as
[Defining and Characterizing Reward Hacking](skalse2022-defining-reward-hacking.md): the proxy you measure becomes the
thing you get.

It also means an honest model is currently penalized by the benchmarks it is judged on,
which is worth sitting with.

## Notes
Short and readable, and unusually direct about the incentive being the field's own rather
than the model's. Pairs well with the uncertainty-estimation work in this collection, since
those methods are the tooling for the abstention this paper argues should be rewarded.
