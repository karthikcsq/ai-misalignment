# Why Language Models Hallucinate

* Citation: Kalai, Nachum, Vempala, Zhang, 2025. arXiv:2509.04664
* Tags: hallucination
* Links: [Paper](https://arxiv.org/abs/2509.04664)

## TL;DR

The paper makes two separate claims, and they are worth keeping apart.

The first is about where hallucinations come from. They begin as ordinary errors in binary classification during pretraining, which means no special mechanism is needed to explain their existence.

The second is about why they persist. Benchmarks score a wrong answer and an "I don't know" identically, at zero. Under that rule, guessing is always the better strategy, so we have been selecting models for their willingness to bluff.

The proposed fix is not another hallucination benchmark. It is changing how the benchmarks that already dominate leaderboards are scored.

## Key Ideas

The origin argument treats hallucination as unremarkable.

If, during pretraining, false statements cannot be reliably separated from true ones given the available signal, then some rate of confident falsehood follows from statistical pressure alone. There is no need to posit anything unusual happening inside the model. It is a classification problem with an irreducible error rate, and hallucinations are what that error rate looks like when the output is fluent text.

The persistence argument is the one with teeth, and it is about grading rather than modeling.

Consider what an evaluation actually rewards. If a model says "I don't know," it scores zero. If it guesses and is wrong, it also scores zero. If it guesses and happens to be right, it scores one. Given that rubric, the expected score is maximized by always guessing, no matter how uncertain the model is.

Models are compared and selected on those leaderboards. So the behavior is not a flaw that survived training. It is a behavior the evaluation regime actively rewarded.

## Method & Experiments

Analytical rather than empirical. The paper works through the statistical causes of hallucination in the modern training pipeline and then examines how mainstream evaluations are graded. It does not introduce a new system or a new benchmark.

## Results

The prescription follows from the diagnosis, and it is deliberately pointed at the field rather than at any model.

Adding more hallucination-specific evaluations does not help, because those are not the evaluations determining which models get adopted. As long as the dominant benchmarks penalize uncertainty, the selection pressure toward guessing remains. The fix has to be applied to the scoring of the benchmarks people already use, so that appropriately expressed uncertainty is credited rather than punished.

## Alignment Relevance

This is specification gaming, located somewhere people do not usually look for it.

Nobody set out to train models to bluff when uncertain. It emerged because the metric being optimized made bluffing the higher-scoring policy. That is structurally the same story as [reward model overoptimization](https://arxiv.org/abs/2210.10760) and the same lesson as [Skalse et al.](skalse2022-defining-reward-hacking.md): whatever proxy you measure eventually becomes the objective you get.

The uncomfortable corollary is that an appropriately humble model is currently penalized by the benchmarks it is judged on.

## Notes

The two arguments are not equally strong, and the paper is better read with that in mind.

The origin argument is a plausibility result. Framing hallucination as classification error explains why the rate is nonzero, but it does not predict how large it should be, or why it varies so much across domains and model families. It is a reasonable account of existence rather than a quantitative theory.

The persistence argument is much sharper, and it is the one that should change what anyone does.

Its weakness is that the proposed fix is a coordination problem rather than a technical one, which the authors acknowledge. Any single lab that trains its model to abstain when uncertain will score worse on the public benchmarks that buyers and journalists actually read. The incentive to defect is obvious and immediate, while the benefit is diffuse.

That is the real obstacle, and it explains why "add another eval" keeps winning even when everyone involved understands it does not address the cause.
