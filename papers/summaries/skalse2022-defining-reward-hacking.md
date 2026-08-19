# Defining and Characterizing Reward Hacking

- Citation: Skalse, Howe, Krasheninnikov, Krueger, 2022. Defining and Characterizing Reward Hacking. arXiv:2209.13085
- Tags: specification-gaming
- Links: [Paper](https://arxiv.org/abs/2209.13085)

## TL;DR
- The first formal definition of reward hacking, and the news is bad.
- A proxy reward is *unhackable* if increasing expected proxy return can never decrease expected true return.
- Over all stochastic policies, two reward functions can only be unhackable if one of them is constant. Unhackability is essentially unavailable in the general case.

## Key Ideas
The intuition most people carry is that you can make a proxy safe by making it narrower:
leave out the terms you are unsure about, ignore distinctions that seem unimportant, and
you get something conservative that cannot be gamed. This paper shows that intuition is
mostly wrong, and shows why.

The reason is structural. Expected reward is linear in state-action visit counts. That
linearity makes unhackability a very strong condition, strong enough that over the full set
of stochastic policies almost nothing satisfies it except trivially.

## Method & Experiments
Theoretical. The contributions are definitions and proofs, not experiments. The paper
defines unhackability, then characterizes when it can hold, then narrows to cases where the
answer is not vacuous.

## Results
Over all stochastic policies, an unhackable pair requires one reward to be constant, which
is useless. Restricting to deterministic policies or to finite sets of stochastic policies,
non-trivial unhackable pairs do exist. The paper gives necessary and sufficient conditions
for *simplifications*, an important special case where a proxy is a legitimate
simplification of the true reward rather than a hackable stand-in.

The framing conclusion is a tension the authors state directly: using reward functions to
specify narrow tasks and using them to align systems with human values pull against each
other.

## Alignment Relevance
This is the paper to cite when someone proposes solving reward hacking by writing a more
careful reward function. The result says the failure is not a lack of care. It also pairs
naturally with the empirical side: [Gao et al.](https://arxiv.org/abs/2210.10760) show the proxy-true gap
widening predictably under optimization pressure, which is what this theory predicts you
should see.

## Notes
Dense but short. The proofs are readable if you are comfortable with MDP notation. If you
only take one thing, take the linearity argument, since it is what makes the negative
result so broad.
