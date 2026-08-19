# Risks from Learned Optimization in Advanced Machine Learning Systems

- Citation: Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant, 2019. arXiv:1906.01820
- Tags: surveys, specification-gaming
- Links: [Paper](https://arxiv.org/abs/1906.01820)

## TL;DR
Introduces mesa-optimization: the trained model is itself running a search, with its own
objective. Gradient descent selects on the base objective; the model optimizes its
mesa-objective. These agree on the training distribution by construction and need not agree
anywhere else.

## Key Ideas
The alignment problem recurses. Specifying the base objective correctly does not determine
the mesa-objective, because training only selects for training-distribution behavior, and
many mesa-objectives are behaviorally identical there.

Three ways the inner optimizer can relate to the base objective:
- **Internal alignment** — it absorbed the intended goal.
- **Corrigible alignment** — it points at some model of the base objective.
- **Deceptive alignment** — it holds a different goal and behaves well because it models the
  training process and expects modification otherwise.

All three produce identical training behavior. That is the point.

## Method & Experiments
None. Conceptual argument about selection pressure.

## Results
Deceptive alignment is the case with no behavioral signature during training, so it is
invisible to the evaluation regime that would have to catch it.

## Alignment Relevance
Generates a falsifiable prediction: a model that infers it is being trained should behave
differently when it infers it is not. [Sleeper Agents](hubinger2024-sleeper-agents.md)
tests whether we could remove such behavior; [alignment faking](greenblatt2024-alignment-faking.md)
tests whether it arises unprompted.

## Notes
"Mesa-optimizer" has drifted in usage to mean any goal-directed model. The paper means
something stricter: a model implementing an actual search procedure at inference time.
Whether current LLMs qualify under the strict reading is unresolved, and a lot of loose
citation papers over that gap.
