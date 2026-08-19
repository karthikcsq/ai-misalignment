# Defeating Prompt Injections by Design

- Citation: Debenedetti, Shumailov, Fan, Hayes et al., 2025. Defeating Prompt Injections by Design. arXiv:2503.18813
- Tags: prompt-injection, security-threats
- Links: [Paper](https://arxiv.org/abs/2503.18813), [Code](https://github.com/google-research/camel-prompt-injection)

## TL;DR
- Stops trying to make the model resist injection and instead builds a system layer where injected text structurally cannot redirect execution.
- Extracts control and data flow from the trusted user query up front, so untrusted data read later can never alter program flow.
- Solves 77% of AgentDojo tasks with provable security, against 84% for an undefended system. The security is a guarantee, not a benchmark score.

## Key Ideas
Nearly every other defense asks the model to be more discerning: mark untrusted text,
train an instruction hierarchy, detect injections. All of these inherit the same weakness,
which is that they degrade to a judgment call by a model that can be argued with.

CaMeL changes the question. The user's query is trusted, so parse *it* into an explicit
program with a defined control flow and data flow. Untrusted content retrieved during
execution is then data flowing through that program. It is never interpreted as
instructions, because the structure that decides what happens next was fixed before any of
it was read.

This is the classic code-versus-data separation that fixed SQL injection, applied to agents.

## Method & Experiments
A custom interpreter wraps the LLM. The trusted query yields a program; the interpreter runs
it. On top of that, CaMeL attaches **capabilities** to data, tracking provenance and
enforcing security policies at tool-call time. That second mechanism handles exfiltration,
which control-flow integrity alone does not: an agent that legitimately reads a private
document should still not be permitted to send it to an arbitrary address.

Evaluation is on AgentDojo, the standard prompt-injection agent benchmark.

## Results
77% of tasks solved with provable security. The undefended baseline solves 84%, so the
defense costs roughly 7 points of capability. That is a real cost and the paper does not
hide it.

The word doing the work is *provable*. Other defenses report an attack success rate that
went down. This one reports a class of attack that cannot succeed against the architecture,
which is a different kind of claim.

## Alignment Relevance
This is the strongest existing argument that prompt injection is a systems problem rather
than a model-training problem. Set against [Ji et al.](https://arxiv.org/abs/2511.15203), who break several
published defenses by adapting to their specific mechanisms, and against
[Abdelnabi and Bagdasarian](https://arxiv.org/abs/2605.17634), who argue injection may be structurally
unavoidable for agents acting on untrusted data, CaMeL is the constructive reply: constrain
the system, not the model.

## Notes
The capability layer is the underrated half. Control-flow integrity gets the attention, but
data exfiltration is the harm most real deployments should worry about first.
