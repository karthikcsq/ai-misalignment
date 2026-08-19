# Defining and Characterizing Reward Hacking

* Citation: Skalse, Howe, Krasheninnikov, Krueger, 2022. arXiv:2209.13085
* Tags: specification-gaming
* Links: [Paper](https://arxiv.org/abs/2209.13085)

## TL;DR

This is the first formal definition of reward hacking, and the main result is a negative one.

A proxy reward is called **unhackable** if increasing the expected proxy return can never decrease the expected true return. That is the property you would want from a safe stand-in objective.

The paper proves that if you consider the full set of stochastic policies, two reward functions can only be unhackable with respect to each other when one of them is constant. In other words, in the general case, a genuinely safe proxy is not available.

## Key Ideas

Most people have an intuition that you can make a proxy reward safer by making it more conservative. Leave out the terms you are unsure about. Ignore fine distinctions between outcomes that seem roughly equivalent. Keep the objective narrow and the agent will have less room to find a loophole.

The paper shows this intuition is mostly wrong, and the reason is structural rather than practical.

Expected reward is linear in state-action visit counts. Unhackability is a claim quantified over a set of policies. When that set is the full stochastic simplex, the linearity makes the condition extremely demanding, so demanding that essentially nothing satisfies it except in the trivial case where one reward function is constant and therefore useless.

So the problem is not that reward designers are careless. Narrowing a reward function does not remove the possibility of divergence between proxy and truth. It usually just moves where that divergence shows up.

## Method & Experiments

Purely theoretical. The contributions are definitions and proofs, and there are no experiments.

## Results

The picture improves once you stop quantifying over every possible stochastic policy.

If you restrict attention to deterministic policies, or to finite sets of stochastic policies, non-trivial unhackable pairs do exist. The paper also gives necessary and sufficient conditions for **simplifications**, which is the important special case where a proxy is a legitimate coarsening of the true reward rather than a substitute that can be exploited.

The authors state the broader tension directly: using reward functions to specify narrow tasks and using them to align systems with human values are pulling in different directions.

## Alignment Relevance

This is the paper to reach for when someone proposes solving reward hacking by writing a better reward function. The result says that approach does not generalize, and it says so for reasons that do not depend on how careful the designer is.

It also pairs naturally with the empirical literature. [Gao et al.](https://arxiv.org/abs/2210.10760) measure the gap between proxy reward and true reward widening predictably as optimization pressure increases, which is exactly the behavior this theory says to expect.

## Notes

The negative result gets cited more loosely than it deserves. People tend to summarize it as "unhackability is impossible," but the theorem is about degeneracy over a particular policy set, not impossibility in general.

The restricted-policy-class results are the more useful half of the paper, and they are routinely skipped. If unhackable pairs exist once you constrain the set of policies under consideration, then the practical lever is not the objective but the optimizer, and specifically how much of the policy space you allow the agent to explore.

That is worth noticing because it is the same conclusion RLHF arrived at by trial and error. KL penalties against a reference policy are, in effect, a way of shrinking the policy set so the proxy stays trustworthy inside it. The theory here gives a reason why that works, rather than treating it as a training trick that happens to help.
