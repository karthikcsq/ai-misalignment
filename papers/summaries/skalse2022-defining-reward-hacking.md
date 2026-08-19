# Defining and Characterizing Reward Hacking

* Citation: Skalse, Howe, Krasheninnikov, Krueger, 2022. arXiv:2209.13085
* Tags: specification-gaming
* Links: [Paper](https://arxiv.org/abs/2209.13085)

## TL;DR

This paper gives a formal definition of reward hacking and proves that, in the general case, a perfectly safe proxy reward is not available.

A proxy reward is called unhackable if improving expected performance on the proxy can never reduce expected performance on the true objective.

That sounds like the property we would want from any reliable stand-in objective.

But if the agent can choose from the full set of stochastic policies, the paper shows that two reward functions can only satisfy this relationship in trivial cases, such as when one of the rewards is constant.

So even a carefully designed proxy can eventually disagree with the thing it is supposed to represent.

## Key Ideas

Suppose we cannot directly specify the outcome we really want, so we use a simpler reward function as a proxy.

For example, we might want a recommender system to show people things they find genuinely worth their time. There is no column in the database for that, so we reward watch time instead. Watch time is easy to measure and it does correlate with the thing we care about, at least until the system discovers that outrage holds attention better than usefulness does.

Or in RLHF, the true objective is a helpful and honest answer, and the proxy is a reward model trained on human ratings. That proxy is reasonable until the policy learns that raters reward confident, longer answers whether or not they are correct.

We might try to make that proxy safer by keeping it narrow. If we are unsure about some part of the true objective, we can leave it out. If several outcomes seem roughly equivalent, we can treat them as the same.

That still does not guarantee that optimizing the proxy will improve the true objective.

The problem comes from comparing policies.

Expected reward depends on how often a policy visits different states and takes different actions. If a proxy and a true reward are not perfectly aligned across all of those possibilities, then there can be policies that look better under the proxy while actually being worse under the true objective.

The paper formalizes this idea using unhackability.

For a proxy to be unhackable, every increase in expected proxy reward must avoid decreasing the true reward.

When the allowed policy space contains all stochastic policies, that condition becomes so restrictive that useful non-trivial reward pairs essentially disappear.

The failure is therefore not just a matter of missing clever edge cases when designing the reward.

A proxy can be reasonable in many situations and still break once optimization searches far enough through the policy space.

## Method & Experiments

This is a theoretical paper.

The authors define reward hacking, formalize different relationships between reward functions, and prove conditions under which one reward can or cannot safely stand in for another.

There are no reinforcement-learning experiments or empirical benchmarks.

## Results

The impossibility result changes when the policy space is restricted.

If the agent is limited to deterministic policies, or to certain finite sets of stochastic policies, non-trivial unhackable reward pairs can exist.

The paper also studies simplifications, where the proxy is a coarser version of the true reward rather than a completely different objective.

For example, a simplified reward might ignore distinctions that matter to the true reward while still preserving enough of its structure to rank the relevant policies correctly.

The authors derive conditions for when these simplifications remain safe over a given policy class.

So the result is not that proxies can never work. It is that their reliability depends on the set of policies the optimizer is allowed to consider.

## Alignment Relevance

Reward hacking cannot generally be solved just by writing a more careful reward function.

A proxy may track the true objective well over familiar policies and still fail once optimization pushes into parts of the policy space where the two come apart.

This matches empirical work on reward-model overoptimization.

As optimization pressure increases, systems can keep improving according to the proxy even after performance on the underlying objective begins to decline.

That is the kind of behavior the theory here predicts.

## Notes

The paper is often summarized as proving that unhackable rewards are impossible. That is too broad. The strongest negative result assumes the full set of stochastic policies. Once the policy class is restricted, useful unhackable relationships can exist.

That shifts some of the attention from reward design to optimization. If a proxy is trustworthy only within a limited region of policy space, then one way to keep it useful is to stop the optimizer from moving too far outside that region.

This gives a useful way to think about KL penalties in RLHF. A KL penalty keeps the trained policy relatively close to a reference policy. That limits how far the optimizer can move while chasing the proxy reward. Under this interpretation, the penalty is not just a training convenience. It can help keep the system inside a region where the proxy is still informative.

A reward function can therefore be good enough under weak optimization and become unreliable under stronger optimization. Proxy quality and optimization strength have to be considered together.
