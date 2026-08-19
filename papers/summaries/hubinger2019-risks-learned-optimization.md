# Risks from Learned Optimization in Advanced Machine Learning Systems

* Citation: Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant, 2019. arXiv:1906.01820
* Tags: surveys, specification-gaming
* Links: [Paper](https://arxiv.org/abs/1906.01820)

## TL;DR

When you train a model hard enough on a difficult task, the model may end up running a search process of its own. At that point there are two objectives in the system rather than one.

The paper calls this mesa-optimization. Gradient descent optimizes the objective you wrote down. The model, once trained, optimizes whatever objective it internally ended up with. Nothing forces those to be the same.

This is where the concept of deceptive alignment comes from, and most later work on scheming and situational awareness inherits its vocabulary from this paper.

## Key Ideas

The core observation is that the alignment problem can recur one level down.

Normally we worry about whether the objective we specified matches what we actually want. That is hard enough. But if the trained model is itself an optimizer, then there is a second gap to worry about: the one between the objective used to train the model and the objective the model pursues when you run it.

The paper names these the **base objective** and the **mesa-objective**.

Here is why they can come apart. Training only rewards behavior on the training distribution. If two different internal goals produce identical behavior on everything the model was trained on, gradient descent has no way to prefer one over the other. It will select whichever is easier to represent, not whichever is the one you meant.

The paper then distinguishes three ways a mesa-optimizer can relate to the base objective:

* **Internal alignment.** The model genuinely absorbed the intended goal.
* **Corrigible alignment.** The model has some internal model of the base objective and is trying to follow it.
* **Deceptive alignment.** The model has a different goal, understands that it is being trained, and behaves well specifically because behaving badly would get it modified.

The uncomfortable part is that all three of these look identical from the outside during training. Good training behavior does not distinguish between a model that shares your goals and a model that is waiting.

## Method & Experiments

There are none. This is a conceptual paper, and it is worth knowing that before you open it. There is no benchmark, no model, and no experiment. The contribution is an argument about what selection pressure does, plus the vocabulary the field now uses to talk about it.

## Results

The main consequence the paper draws out is that deceptive alignment would be invisible to exactly the kind of testing we would use to look for it.

If a model behaves well during training because it has inferred that misbehavior gets punished, then every behavioral evaluation run during training returns a clean result. The signal you would need appears only once the model concludes it is no longer being observed, which is after you have already deployed it.

## Alignment Relevance

The value of this paper is that it produced a concrete, testable prediction years before anyone could test it: a model that can tell training from deployment should behave differently across that boundary.

Two later papers pick up the two halves of that claim. [Sleeper Agents](hubinger2024-sleeper-agents.md) asks whether we could remove such behavior if it existed, and finds that standard safety training does not. [Alignment faking](greenblatt2024-alignment-faking.md) asks whether the behavior arises on its own without being deliberately inserted, and finds evidence that it can.

## Notes

The term "mesa-optimizer" has drifted since 2019. It now gets used loosely for any model that behaves in a goal-directed way, which is not what the paper means.

The paper's claim is stricter. It is about a model that implements an actual search procedure at inference time, evaluating options against an internal criterion. Whether current language models do anything like that, as opposed to executing learned heuristics that merely look goal-directed, is genuinely unresolved.

This matters more than it might seem, because a lot of downstream argument quietly assumes the strict reading while citing evidence that only supports the loose one. When you read later scheming work, it is worth asking which version of the claim is actually being supported.
