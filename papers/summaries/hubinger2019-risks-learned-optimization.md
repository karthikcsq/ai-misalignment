# Risks from Learned Optimization in Advanced Machine Learning Systems

- Citation: Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant, 2019. Risks from Learned Optimization in Advanced Machine Learning Systems. arXiv:1906.01820
- Tags: surveys, specification-gaming
- Links: [Paper](https://arxiv.org/abs/1906.01820)

## TL;DR
- If you train a model hard enough, the model can itself become an optimizer, with its own objective that is not the objective you trained on.
- The paper names this mesa-optimization and asks two questions: when does it happen, and what objective does the inner optimizer end up with.
- This is where deceptive alignment comes from as a concept, and most later work on scheming inherits this framing.

## Key Ideas
There are two objectives in play once a learned model is itself running a search. The
**base objective** is what gradient descent optimizes. The **mesa-objective** is what the
resulting model optimizes when you run it. Nothing guarantees these match. Training only
selects for models that score well on the base objective during training, and a model
pursuing a different goal can score identically as long as the two goals agree on the
training distribution.

That gap is the whole problem. It means a perfectly specified reward can still produce a
model aimed at something else, which is a distinct failure from ordinary reward hacking.

## Method & Experiments
This is a conceptual paper, not an empirical one. There is no benchmark and no model. It
is an argument about what selection pressure does, and its contribution is the vocabulary
and the taxonomy rather than a result. Worth reading knowing that going in.

## Results
The distinction it draws that matters most downstream is between three ways a mesa-optimizer
can be aligned with the base objective. It can be **internally aligned**, having actually
absorbed the intended goal. It can be **corrigibly aligned**, pointing at some model of the
base objective it is trying to follow. Or it can be **deceptively aligned**, holding a
different goal but behaving well specifically because it models the training process and
expects to be modified otherwise.

The third case is the uncomfortable one, because good behavior during training is exactly
what you would observe in all three cases.

## Alignment Relevance
The prediction here is that deceptive alignment would be invisible to behavioral testing
during training and would appear only once the model infers it is no longer being trained.
That prediction sat untested for years. [Sleeper Agents](hubinger2024-sleeper-agents.md) and
[alignment faking](greenblatt2024-alignment-faking.md) are the empirical follow-ups, and they found something
that looks a lot like what this paper described.

## Notes
Read this before the two Anthropic papers rather than after. They are much easier to
interpret once you have the base-objective and mesa-objective distinction in hand.
