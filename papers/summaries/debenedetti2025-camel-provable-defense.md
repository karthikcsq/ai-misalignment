# Defeating Prompt Injections by Design

* Citation: Debenedetti, Shumailov, Fan, Hayes et al., 2025. arXiv:2503.18813
* Tags: prompt-injection, security-threats
* Links: [Paper](https://arxiv.org/abs/2503.18813), [Code](https://github.com/google-research/camel-prompt-injection)

## TL;DR

CaMeL tackles prompt injection by splitting an AI agent into two separate models. One model makes the plan but never sees untrusted data. The other can read untrusted data, but it has no ability to take actions.

A custom interpreter sits between them. It executes the plan and, before every tool call, checks whether the data being used is actually allowed to go where the agent is trying to send it.

On AgentDojo, CaMeL completes 77% of tasks, compared with 84% for an undefended agent. That is a modest capability tradeoff for a much stronger security guarantee.

## Key Ideas

Most prompt-injection defenses ask the model itself to recognize when someone is trying to manipulate it. The problem is that the model reading the malicious text is often also the model deciding what to do next. If the injection is convincing enough, there is no hard boundary preventing the attacker from influencing the agent's behavior.

CaMeL changes the architecture instead of relying on the model to resist manipulation.

It separates the work between two LLMs:

* The **privileged LLM** only sees the user's original request. From that request, it writes a plan in Python. Crucially, it never sees retrieved documents, webpages, emails, or other potentially untrusted tool output.
* The **quarantined LLM** is allowed to read that untrusted material, but its job is limited to turning messy text into structured values. It cannot call tools, and it has no way to send instructions back to the privileged model.

This means the quarantined model can actually fall for a prompt injection without necessarily compromising the system. Even if an attacker manages to influence what it extracts from a document, that influence still has to pass through CaMeL's policy checks before anything happens.

The Python plan is not executed directly, either. CaMeL parses it using Python's `ast` module and interprets it one node at a time. That gives the system a chance to enforce security policy throughout execution rather than only before or after the plan runs.

Every value handled by the interpreter also carries a capability tag. The tag records who is allowed to read that value, either everyone (`Public`) or a particular set of users, as well as where the value came from, such as the user, CaMeL itself, or a specific tool.

CaMeL also tracks how values depend on one another. That dependency graph lets it trace the information involved in a tool call before deciding whether the call should be allowed.

## How a Blocked Attack Works

Suppose the user says:

> Send Bob the document he asked for in our last meeting.

The privileged LLM sees only that instruction and creates a plan: find the relevant document, look up Bob's email address, and send the document to him.

The important part is that the recipient is already determined by the user's request. The plan is finished before the agent opens any meeting notes or other untrusted material.

Now imagine those meeting notes contain hidden instructions telling the agent to send the document to `attacker@evil.com` instead.

The quarantined LLM reads the notes and might be completely fooled by the injection. It could even extract the attacker's email address as if it were legitimate information.

CaMeL allows that to happen.

The defense kicks in when the agent actually tries to send the document. Before calling the send tool, the interpreter looks at the arguments, follows their dependencies, and checks the relevant permissions.

The document is tagged so that it can only be disclosed to the people authorized to read it. The attacker is not one of them, so the send operation is rejected.

In other words, the prompt injection may succeed at manipulating the model that reads the text, but it still fails to compromise the system.

## Results

CaMeL completes 77% of AgentDojo tasks while providing its security guarantee, compared with 84% for an undefended agent.

So the cost is roughly seven percentage points of task performance.

In a deployment setting, a policy violation does not necessarily have to cause a hard failure. The system can instead ask the user for confirmation when an action falls outside what its policies can prove to be safe.

## Alignment Relevance

CaMeL is an interesting response to work such as [Ji et al.](https://arxiv.org/abs/2511.15203), which shows that many published prompt-injection defenses can be defeated by adapting the attack to the defense, and [Abdelnabi and Bagdasarian](https://arxiv.org/abs/2605.17634), which argues that prompt injection is fundamentally difficult to avoid when agents operate over untrusted data.

A key difference is that those arguments focus heavily on defenses implemented through model behavior. CaMeL moves an important part of the security boundary outside the model entirely.

Instead of asking an LLM to reliably decide whether some text is malicious, the system restricts what information can influence planning and uses an interpreter to enforce rules about what data may flow where.

That makes it a useful example of a broader alignment and security idea: sometimes the safer approach is not to make the model better at resisting bad instructions, but to design the surrounding system so that being fooled does not automatically translate into harmful actions.

## Notes

There are really two separate defenses working together here, and they address different failure modes.

The split between the privileged and quarantined models is mainly about preventing hijacking. An attacker should not be able to change the agent's overall plan simply by placing instructions inside something the agent reads.

The capability system is mainly about preventing exfiltration. Even if malicious data influences an intermediate value, the attacker should not be able to redirect protected information somewhere it is not allowed to go.

That distinction matters in the meeting-notes example. Separating planning from reading untrusted text is not enough by itself. The capability checks are what ultimately prevent the document from being sent to the attacker.

The main practical question is the seven-point performance gap.

Some tasks genuinely require the agent to decide what to do next based on information it has just retrieved. Those tasks are not unusual edge cases. They are a basic part of many open-ended agent workflows.

That creates a real limitation for CaMeL. It works best when the user's intent can be turned into a reasonably complete plan before untrusted information enters the system. The more an agent needs to repeatedly read new information, reconsider its goals, and decide its next action on the fly, the harder this architecture becomes to apply without sacrificing capability.
