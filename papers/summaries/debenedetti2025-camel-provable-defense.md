# Defeating Prompt Injections by Design

- Citation: Debenedetti, Shumailov, Fan, Hayes et al., 2025. arXiv:2503.18813
- Tags: prompt-injection, security-threats
- Links: [Paper](https://arxiv.org/abs/2503.18813), [Code](https://github.com/google-research/camel-prompt-injection)

## TL;DR
Extracts control and data flow from the trusted query into an explicit program before any
untrusted data is read, so retrieved content cannot alter execution. 77% of AgentDojo tasks
solved with provable security against 84% undefended.

## Key Ideas
Every prompt-level defense terminates in a judgment call by a model that can be argued with.
CaMeL removes the model from the security decision: the trusted query is parsed into a
program, the interpreter executes it, and untrusted content is data flowing through a
control flow fixed before it arrived.

Code-versus-data separation, the fix that settled SQL injection, applied to agents.

## Method & Experiments
A custom interpreter wraps the LLM. Capabilities attach to values, tracking provenance and
enforcing policy at tool-call boundaries. Evaluated on AgentDojo.

## Results
77% task completion with provable security, 84% undefended, so roughly 7 points of
capability traded for the guarantee. The claim is a class of attack that cannot succeed
against the architecture, not a reduced attack success rate.

## Alignment Relevance
The constructive counterpoint to [Ji et al.](https://arxiv.org/abs/2511.15203), who break
published defenses by adapting to each mechanism, and to
[Abdelnabi and Bagdasarian](https://arxiv.org/abs/2605.17634), who argue injection is
structurally unavoidable for agents over untrusted data. Both hold if the defense lives in
the model; neither bites an interpreter.

## Notes
The capability layer is doing more work than the control-flow story it gets credited for.
Control-flow integrity stops hijacking; exfiltration is the harm most deployments should
rank first, and only provenance tracking addresses it. An agent legitimately reading a
private document still must not be able to send it anywhere.

The 7-point capability gap is what determines adoption, and it comes from tasks whose control
flow genuinely depends on retrieved content. Those are not pathological, which bounds how
general this approach can be. It also requires the query to be parseable into a program up
front, so open-ended agent loops are a poor fit.
