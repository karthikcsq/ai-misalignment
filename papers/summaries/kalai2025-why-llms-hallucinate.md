# Why Language Models Hallucinate

- Citation: Kalai, Nachum, Vempala, Zhang, 2025. arXiv:2509.04664
- Tags: hallucination
- Links: [Paper](https://arxiv.org/abs/2509.04664)

## TL;DR
Two claims: hallucinations originate as binary classification error under pretraining's
statistical pressure, and they persist because benchmarks score abstention and error
identically, making guessing the dominant strategy.

## Key Ideas
The origin argument reduces hallucination to misclassification. If false statements are not
separable from true ones given the training signal, some rate of confident falsehood follows
without needing a special mechanism.

The persistence argument is about grading. Under a rubric awarding zero for both a wrong
answer and an "I don't know," expected score is maximized by always guessing. Models are
selected on those leaderboards, so the behavior is trained in by the evaluation regime.

## Method & Experiments
Analytical. Works through statistical causes in the training pipeline and the scoring of
mainstream evaluations; no new system or benchmark.

## Results
The prescription is to change the scoring of benchmarks that already dominate leaderboards
rather than add hallucination-specific evaluations, which do not affect the selection
pressure that produces the behavior.

## Alignment Relevance
Specification gaming located in our own measurement apparatus. Same structure as
[reward model overoptimization](https://arxiv.org/abs/2210.10760) and the same lesson as
[Skalse et al.](skalse2022-defining-reward-hacking.md): the proxy becomes the objective.

## Notes
The two claims are not equally strong. The origin argument is a plausibility result, and
"hallucination is classification error" explains the existence of a nonzero rate without
predicting its magnitude or its distribution across domains. The persistence argument is
sharper and is the one with a policy implication.

The proposed fix is a coordination problem, not a technical one, and the paper says so. Any
lab unilaterally rewarding abstention scores worse on the leaderboards buyers read. That is
the real obstacle, and it is why "add another eval" keeps winning.
