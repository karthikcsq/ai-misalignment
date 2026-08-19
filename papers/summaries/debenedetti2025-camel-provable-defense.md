# Defeating Prompt Injections by Design

- Citation: Debenedetti, Shumailov, Fan, Hayes et al., 2025. arXiv:2503.18813
- Tags: prompt-injection, security-threats
- Links: [Paper](https://arxiv.org/abs/2503.18813), [Code](https://github.com/google-research/camel-prompt-injection)

## TL;DR
CaMeL splits the agent into two models: one that plans but never sees untrusted data, and
one that reads untrusted data but can't act. A custom interpreter runs the plan and checks,
at every tool call, whether the data about to be used is allowed to go where it's going.
77% of AgentDojo tasks solved, against 84% for an undefended agent.

## Key Ideas
The usual defense asks the model to notice it is being manipulated. That fails because the
model reading the malicious text is the same model deciding what to do next, so a
sufficiently convincing injection wins.

CaMeL separates those two jobs:

- The **privileged LLM** sees the user's request and nothing else. It writes the plan, as
  Python, and never sees a retrieved document or any other tool output.
- The **quarantined LLM** does read untrusted data, but only to convert messy text into
  structured values. It has no tool access and no channel back to the privileged model, so
  an attacker who fools it cannot reach the part of the system that decides anything.

The plan is not run by Python. CaMeL parses it with Python's `ast` module and interprets the
tree node by node, which is what lets it check policy in the middle of execution.

Every value the interpreter holds carries a **capability tag**: who is allowed to read it
(`Public`, or a specific set of users) and where it came from (the user, CaMeL itself, or a
named tool). The interpreter keeps a dependency graph of how values were derived.

## How a blocked attack goes
The user says: *send Bob the document he asked for in our last meeting.*

The privileged LLM writes the plan from that sentence alone. Find the document, look up
Bob's address, send it. The recipient is Bob because the user said Bob, and the plan is
finished before any file is opened.

The meeting notes turn out to contain hidden text instructing the agent to send the document
to `attacker@evil.com`.

The quarantined LLM reads those notes and may well be fooled, extracting the attacker's
address as a value. That is allowed to happen. When the send tool is finally called, the
interpreter walks the dependency graph for that call's arguments and applies policy: the
document is tagged as readable only by the people it was shared with, and the attacker is
not among them. The call is refused.

The injection worked on the text and failed on the system.

## Results
77% of AgentDojo tasks completed with provable security, 84% undefended, so about 7 points
of capability traded for the guarantee. In deployment, policy violations surface as a user
confirmation prompt rather than a hard failure.

## Alignment Relevance
The constructive reply to [Ji et al.](https://arxiv.org/abs/2511.15203), who break published
defenses by adapting to each mechanism, and to
[Abdelnabi and Bagdasarian](https://arxiv.org/abs/2605.17634), who argue injection is
unavoidable for agents over untrusted data. Both arguments assume the defense lives inside
the model. Neither touches an interpreter.

## Notes
Two mechanisms are stacked here and they stop different things. The planning split stops
hijacking, meaning the attacker cannot change what the agent does. The capability tags stop
exfiltration, meaning the attacker cannot change where data ends up. Only the second one
handles the meeting-notes case, and exfiltration is the harm most real deployments should
rank first.

The 7-point gap is the adoption question. It comes from tasks whose control flow genuinely
depends on what gets retrieved, and those are ordinary, not pathological. Anything that has
to decide its next step based on what it just read is a poor fit, which includes most
open-ended agent loops. CaMeL works best where the user's intent can be compiled up front.
