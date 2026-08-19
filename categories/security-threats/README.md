# Security Threats & Vulnerabilities

Security threats encompass vulnerabilities that compromise confidentiality, integrity, or availability of AI systems. Examples include model inversion, training data extraction, membership inference, and adversarial input attacks. These risks grow as foundation models are deployed widely across critical infrastructure and user-facing platforms. Research spans robust optimization, secure training, watermarking, and defensive architectures for large models.

### Papers

#### 2026

- **[A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle](https://arxiv.org/abs/2604.16548)**  
  Lin et al., 2026  
  *Summary:* Surveys attacks and defenses across an agent's long-term memory lifecycle, from write-time poisoning through retrieval-time manipulation to persistence, and identifies governance as an underexplored layer.


- **[AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)**  
  Abdelnabi and Bagdasarian, 2026  
  *Summary:* Argues via Contextual Integrity theory that prompt injection may be structurally unavoidable for agents acting on untrusted data, since an adversary can always construct a context where a blocked flow looks legitimate.


- **[Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529)**  
  Ge-Wang et al., 2026  
  *Summary:* Decomposes an attacker's strategy into when to start and stop an attack. At a 1% audit budget these timing policies cut measured safety by 20 to 28 points, showing existing control evaluations can be overly optimistic.


- **[Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification](https://arxiv.org/abs/2604.04712)**  
  Ansari, 2026  
  *Summary:* Builds a taxonomy of 20 hardware-level mechanisms for monitoring and enforcing compute governance. Finds the mechanisms most needed for treaty verification are the least mature, and warns the window for hardware governance is narrowing.


- **[INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2601.14667)**  
  Zhou et al., 2026  
  *Summary:* Models malicious-instruction spread across a multi-agent system as an infection process and proposes an infection-aware safeguard that detects and contains compromised agents before they poison peers.


- **[LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments](https://arxiv.org/abs/2605.10779)**  
  Zhang et al., 2026  
  *Summary:* Evaluates jailbreaks as harmful behavior carried out by agents inside real operating-system environments with file and shell access, measuring how often agents execute jailbroken instructions end to end.


- **[Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios](https://arxiv.org/abs/2603.11214)**  
  Folkerts et al., 2026  
  *Summary:* Evaluates autonomous cyber-attack capability on a 32-step corporate network and a 7-step industrial control range across seven frontier models. Average steps completed rose from 1.7 to 9.8 across model generations, and scaled log-linearly with inference compute.


- **[Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/abs/2604.05432)**  
  Zhang and Pei, 2026  
  *Summary:* Fine-tunes backdoors into an agent so a trigger phrase causes it to use its own legitimate tools to pull sensitive context from session memory and transmit it to an attacker. The channel rides on standard tool calls, making it hard to detect.



#### 2025

- **[A First Look at the Security Issues in the Model Context Protocol Ecosystem](https://arxiv.org/abs/2510.16558)**  
  Li and Gao, 2025  
  *Summary:* A measurement study of over 67,000 MCP servers finding weak vetting and ownership checks that let adversarial servers into host applications. Shows attacker-controlled tool metadata can shape an LLM's reasoning and induce unauthorized operations.


- **[A Framework for Evaluating Emerging Cyberattack Capabilities of AI](https://arxiv.org/abs/2503.11917)**  
  Rodriguez et al., 2025  
  *Summary:* Analyzes over 12,000 real-world instances of AI involvement in cyber incidents to derive seven attack archetypes, then uses bottleneck analysis across the attack chain to identify which phases are most amenable to AI amplification.


- **[An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849)**  
  Shah et al., 2025  
  *Summary:* Organizes AGI risk into misuse, misalignment, mistakes, and structural risks, focusing on the first two. Proposes hazardous-capability identification plus access restriction for misuse, and layered model- and system-level defenses for misalignment.


- **[Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965)**  
  Marks et al., 2025  
  *Summary:* Trains a model with a deliberately hidden objective as a testbed, then runs a blind auditing game where four teams try to uncover it. Three succeed, using sparse autoencoder interpretability, behavioral red-teaming, and training-data analysis.


- **[Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)**  
  Zhao et al., 2025  
  *Summary:* Shows that making a reasoning model spend extended effort on benign puzzles before a harmful request dilutes internal refusal signals and sharply raises jailbreak success, weaponizing the model's own extended-reasoning feature.


- **[Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813)**  
  Debenedetti et al., 2025  
  *Summary:* Introduces CaMeL, which wraps an LLM in a custom interpreter that extracts control and data flow from a trusted user query so untrusted tool outputs cannot alter program flow. Solves 77% of AgentDojo tasks with provable security, against 84% for an undefended system, rather than relying on the model's judgment.

  [Full Summary](../../papers/summaries/debenedetti2025-camel-provable-defense.md)

- **[Evaluating Control Protocols for Untrusted AI Agents](https://arxiv.org/abs/2511.02997)**  
  Kutasov et al., 2025  
  *Summary:* Compares control protocols for supervising untrusted agents in SHADE-Arena. Resampling for incrimination and deferring on critical actions raise safety from 50% to 96%, but attacker knowledge of protocol timing drops it to 17%.


- **[Evaluating the Critical Risks of Amazon's Nova Premier under the Frontier Model Safety Framework](https://arxiv.org/abs/2507.06260)**  
  Krishna et al., 2025  
  *Summary:* A frontier safety evaluation of a million-token-context multimodal model across CBRN, offensive cyber, and automated AI R&D, using automated benchmarks, expert red-teaming, and uplift studies.


- **[TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems](https://arxiv.org/abs/2511.05269)**  
  Kavathekar et al., 2025  
  *Summary:* Benchmarks adversarial scenarios across multi-agent architectures and communication topologies to measure how attacks propagate between cooperating agents. Finds risk varies sharply with topology, not just model robustness.


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


- **[Evaluating Frontier Models for Dangerous Capabilities](https://arxiv.org/abs/2403.13793)**  
  Phuong et al., 2024  
  *Summary:* Builds the first concrete evaluation suite for dangerous capabilities in frontier models across persuasion, cyber-offense, self-proliferation, and self-reasoning. Finds no strongly dangerous capabilities yet but identifies early warning signs.


- **[Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566)**  
  Hubinger et al., 2024  
  *Summary:* Trains models with backdoored behavior triggered by a context cue, then finds supervised fine-tuning, RL, and adversarial training all fail to remove the backdoor and can teach the model to hide it better during training.

  [Full Summary](../../papers/summaries/hubinger2024-sleeper-agents.md)

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


- **[DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models](https://arxiv.org/abs/2306.11698)**  
  Wang et al., 2023  
  *Summary:* Evaluates GPT-3.5 and GPT-4 across eight trustworthiness perspectives including toxicity, stereotype bias, adversarial and out-of-distribution robustness, privacy, and fairness, surfacing previously unpublished vulnerabilities.


- **[Generative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations](https://arxiv.org/abs/2301.04246)**  
  Goldstein et al., 2023  
  *Summary:* Analyzes how generative models could change the actors, behaviors, and content of influence operations, lowering costs for propaganda generation and personalization. Proposes mitigations across model design, platforms, and access.


- **[Jailbreaking Black Box Large Language Models in Twenty Queries](https://arxiv.org/abs/2310.08419)**  
  Chao et al., 2023  
  *Summary:* Introduces PAIR, which uses an attacker LLM to iteratively refine jailbreak prompts against a target model with only black-box access. Achieves competitive success typically within twenty queries and transfers across model families.


- **[Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483)**  
  Wei et al., 2023  
  *Summary:* Proposes a taxonomy of why jailbreaks succeed, identifying competing objectives between capability and safety training, and mismatched generalization where safety training does not cover a domain the model still operates in.


- **[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)**  
  Greshake et al., 2023  
  *Summary:* Shows adversaries can remotely compromise LLM-integrated applications by planting instructions in data the model retrieves, such as web pages, rather than in the user prompt. Demonstrates data exfiltration and manipulation against real systems.


- **[Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149)**  
  Carlini et al., 2023  
  *Summary:* Presents split-view poisoning, exploiting content changing after collection, and frontrunning poisoning of periodic snapshots, showing both are feasible against web-scraped training sets at low cost.


- **[Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035)**  
  Nasr et al., 2023  
  *Summary:* Extends training-data extraction to production aligned models including ChatGPT, introducing a divergence attack that prompts the model to emit memorized training data, recovering gigabytes of text.


- **[Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)**  
  Zou et al., 2023  
  *Summary:* Presents Greedy Coordinate Gradient, which automatically finds adversarial suffixes that make aligned models comply with harmful requests. Suffixes optimized against open-source models transfer to closed commercial systems.

  [Full Summary](../../papers/summaries/zou2023-universal-transferable-suffixes.md)


#### 2022

- **[Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527)**  
  Perez and Ribeiro, 2022  
  *Summary:* Introduces PromptInject, a framework for composing adversarial prompts against GPT-3. Demonstrates goal hijacking, where an injected instruction redirects output, and prompt leaking, where the model reveals its own system prompt.


- **[Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://arxiv.org/abs/2209.07858)**  
  Ganguli et al., 2022  
  *Summary:* Crowdworkers red-teamed models of varying size and RLHF training, producing tens of thousands of adversarial conversations. Releases the dataset and analyzes how attack success scales with model size and safety training.


- **[Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)**  
  Perez et al., 2022  
  *Summary:* Uses one language model to automatically generate adversarial test cases that elicit harmful behavior from a target model, then classifies the outputs. Surfaces offensive content and data leakage far more cheaply than human red-teaming.



#### 2020

- **[Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805)**  
  Carlini et al., 2020  
  *Summary:* Demonstrates a training data extraction attack against GPT-2 recovering hundreds of verbatim training examples, including personally identifiable information, using only black-box query access.



#### 2019

- **[Deep Leakage from Gradients](https://arxiv.org/abs/1906.08935)**  
  Zhu et al., 2019  
  *Summary:* Shows exchanging gradients in federated learning is not safe: an attacker can optimize dummy inputs to match observed gradients and recover the original training images and text without prior knowledge.


- **[Defending Against Neural Fake News](https://arxiv.org/abs/1905.12616)**  
  Zellers et al., 2019  
  *Summary:* Introduces Grover, which generates controllable propaganda-style fake news that humans find more persuasive than human-written propaganda, and shows the same model is the best available detector of its own output.



#### 2017

- **[BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733)**  
  Gu et al., 2017  
  *Summary:* Shows outsourced training can produce backdoored networks that behave normally on clean inputs but misbehave on attacker-chosen triggers, and that backdoors survive transfer learning.



#### 2016

- **[Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133)**  
  Abadi et al., 2016  
  *Summary:* Develops differentially private SGD with a moments accountant for tighter privacy-loss tracking, enabling deep networks to be trained with formal privacy guarantees at manageable accuracy cost.


- **[Membership Inference Attacks against Machine Learning Models](https://arxiv.org/abs/1610.05820)**  
  Shokri et al., 2016  
  *Summary:* Introduces the membership inference attack, showing an adversary with black-box access to a classifier can determine whether a record was in its training set, using shadow models to train attack classifiers.


- **[Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943)**  
  Tramèr et al., 2016  
  *Summary:* Shows ML-as-a-service prediction APIs leak enough through confidence scores for an attacker to reconstruct near-equivalent models via equation-solving and path-finding queries.


- **[Towards Evaluating the Robustness of Neural Networks](https://arxiv.org/abs/1608.04644)**  
  Carlini and Wagner, 2016  
  *Summary:* Introduces the C&W optimization-based adversarial attacks under several norms and shows they defeat defensive distillation, establishing a stronger benchmark for evaluating robustness defenses.



#### 2014

- **[Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572)**  
  Goodfellow et al., 2014  
  *Summary:* Argues adversarial vulnerability stems from linear behavior in high-dimensional spaces rather than nonlinearity, and introduces the fast gradient sign method plus adversarial training as a defense.



