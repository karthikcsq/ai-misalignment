# Defining and Characterizing Reward Hacking

- Citation: Skalse, Howe, Krasheninnikov, Krueger, 2022. arXiv:2209.13085
- Tags: specification-gaming
- Links: [Paper](https://arxiv.org/abs/2209.13085)

## TL;DR
A proxy is *unhackable* if increasing expected proxy return can never decrease expected true
return. Over all stochastic policies, an unhackable pair requires one reward to be constant.

## Key Ideas
Expected reward is linear in state-action visit counts. Unhackability quantifies over a
policy set, and over the full stochastic simplex that linearity forces the condition to
degenerate.

This kills the standard intuition that a narrower proxy is a safer one. Dropping terms or
collapsing near-equivalent outcomes does not buy safety; it usually just relocates where the
proxy and the true reward diverge.

## Method & Experiments
Theoretical. Definitions and proofs, no experiments.

## Results
Non-trivial unhackable pairs exist once you restrict to deterministic policies or finite
sets of stochastic policies. The paper gives necessary and sufficient conditions for
*simplifications*, the case where a proxy is a legitimate coarsening rather than a hackable
substitute.

## Alignment Relevance
Closes off "write a more careful reward function" as a general solution. The failure is
structural, not a lack of diligence.

## Notes
The negative result is usually cited as if unhackability is impossible. It isn't; it's
degenerate *over that policy set*. The restricted-policy-class results are the useful half
and get skipped almost every time. Practically this points at constraining the optimizer,
not perfecting the objective, which is the same conclusion RLHF arrived at empirically via
KL penalties.
