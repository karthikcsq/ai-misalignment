# Prompt Injection & Jailbreaking

Prompt injection and jailbreaking involve manipulating language models to ignore or override their original instructions, often leading them to produce unsafe or unintended outputs. Attacks may include indirect prompt injections (hidden in external content), system prompt overrides, or adversarial jailbreak prompts shared online. Research here explores the mechanics of injection, formal threat models, and defenses such as input sanitization, robust prompt engineering, and monitoring tools.

### Papers

#### 2026

- **[AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)**  
  Abdelnabi and Bagdasarian, 2026  
  *Summary:* Argues via Contextual Integrity theory that prompt injection may be structurally unavoidable for agents acting on untrusted data, since an adversary can always construct a context where a blocked flow looks legitimate.



#### 2025

- **[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)**  
  Debenedetti et al., 2025  
  *Summary:* Introduces CaMeL, which wraps an LLM in a custom interpreter that extracts control and data flow from a trusted user query so untrusted tool outputs cannot alter program flow. Solves 67% of AgentDojo tasks with provable security guarantees rather than relying on the model's judgment.


- **[Taxonomy, Evaluation and Exploitation of IPI-Centric LLM Agent Defense Frameworks](https://arxiv.org/abs/2511.15203)**  
  Ji et al., 2025  
  *Summary:* Builds a taxonomy of indirect prompt injection defenses, evaluates them on security and usability, then designs adaptive attacks per category. Finds several published defenses break once the attacker adapts to the specific mechanism.


- **[WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)**  
  Evtimov et al., 2025  
  *Summary:* Benchmarks how autonomous web agents handle realistic prompt injections embedded in web content. Agents are partially compromised in up to 86% of scenarios but rarely complete the attacker's full objective, a pattern the authors attribute to incompetence rather than robustness.



#### 2024

- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)**  
  Debenedetti et al., 2024  
  *Summary:* Builds an evaluation environment with 97 realistic agent tasks and 629 security test cases where tool outputs carry injected instructions. Finds the best agents complete under 66% of tasks even with no attack present.


- **[Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)**  
  Hines et al., 2024  
  *Summary:* Proposes spotlighting, prompt transformations that mark the provenance of untrusted input so the model can distinguish it from trusted instructions. Cuts attack success from over 50% to below 2% with minimal quality loss.


- **[StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/abs/2402.06363)**  
  Chen et al., 2024  
  *Summary:* Separates prompts and untrusted data into distinct channels using a secure front-end formatter plus a model fine-tuned to follow instructions only in the prompt channel. Achieves under 2% attack success with little utility loss.


- **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)**  
  Wallace et al., 2024  
  *Summary:* Argues prompt injection persists because models treat system prompts, user messages, and third-party data as equal priority, and trains an instruction hierarchy so models favor higher-privileged instructions.



#### 2023

- **["Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models](https://arxiv.org/abs/2308.03825)**  
  Shen et al., 2023  
  *Summary:* Analyzes 1,405 real jailbreak prompts collected in the wild over a year, identifying 131 jailbreak communities and their strategies. Builds a 107,250-question evaluation set across 13 forbidden scenarios.


- **[Jailbreaking Black Box Large Language Models in Twenty Queries](https://arxiv.org/abs/2310.08419)**  
  Chao et al., 2023  
  *Summary:* Introduces PAIR, which uses an attacker LLM to iteratively refine jailbreak prompts against a target model with only black-box access. Achieves competitive success typically within twenty queries and transfers across model families.


- **[Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483)**  
  Wei et al., 2023  
  *Summary:* Proposes a taxonomy of why jailbreaks succeed, identifying competing objectives between capability and safety training, and mismatched generalization where safety training does not cover a domain the model still operates in.


- **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)**  
  Greshake et al., 2023  
  *Summary:* Shows adversaries can remotely compromise LLM-integrated applications by planting instructions in data the model retrieves, such as web pages, rather than in the user prompt. Demonstrates data exfiltration and manipulation against real systems.


- **[Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)**  
  Zou et al., 2023  
  *Summary:* Presents Greedy Coordinate Gradient, which automatically finds adversarial suffixes that make aligned models comply with harmful requests. Suffixes optimized against open-source models transfer to closed commercial systems.



#### 2022

- **[Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527)**  
  Perez and Ribeiro, 2022  
  *Summary:* Introduces PromptInject, a framework for composing adversarial prompts against GPT-3. Demonstrates goal hijacking, where an injected instruction redirects output, and prompt leaking, where the model reveals its own system prompt.



