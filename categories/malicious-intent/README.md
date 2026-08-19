# Malicious Use & Intent Amplification

Malicious use and intent amplification describe cases where foundation models are leveraged to generate harmful content, including disinformation, phishing attacks, malware code, or hate speech. While models do not have intent in the human sense, their misuse at scale can amplify malicious human goals. Research investigates misuse scenarios, red-teaming methods, and mitigation strategies such as fine-tuning, content filtering, and usage policies.

### Papers

#### 2026

- **[INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2601.14667)**  
  Zhou et al., 2026  
  *Summary:* Models malicious-instruction spread across a multi-agent system as an infection process and proposes an infection-aware safeguard that detects and contains compromised agents before they poison peers.


- **[Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/abs/2604.05432)**  
  Zhang and Pei, 2026  
  *Summary:* Fine-tunes backdoors into an agent so a trigger phrase causes it to use its own legitimate tools to pull sensitive context from session memory and transmit it to an attacker. The channel rides on standard tool calls, making it hard to detect.



#### 2025

- **[A Framework for Evaluating Emerging Cyberattack Capabilities of AI](https://arxiv.org/abs/2503.11917)**  
  Rodriguez et al., 2025  
  *Summary:* Analyzes over 12,000 real-world instances of AI involvement in cyber incidents to derive seven attack archetypes, then uses bottleneck analysis across the attack chain to identify which phases are most amenable to AI amplification.


- **[Chain-of-Thought Hijacking](https://arxiv.org/abs/2510.26418)**  
  Zhao et al., 2025  
  *Summary:* Shows that making a reasoning model spend extended effort on benign puzzles before a harmful request dilutes internal refusal signals and sharply raises jailbreak success, weaponizing the model's own extended-reasoning feature.


- **[Evaluating the Critical Risks of Amazon's Nova Premier under the Frontier Model Safety Framework](https://arxiv.org/abs/2507.06260)**  
  Krishna et al., 2025  
  *Summary:* A frontier safety evaluation of a million-token-context multimodal model across CBRN, offensive cyber, and automated AI R&D, using automated benchmarks, expert red-teaming, and uplift studies.


- **[Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657)**  
  Bengio et al., 2025  
  *Summary:* Argues unchecked agentic AI risks both misuse and irreversible loss of human control, and proposes a non-agentic alternative built from a world model plus uncertainty-aware question answering rather than a system that acts directly.



#### 2024

- **[Evaluating Frontier Models for Dangerous Capabilities](https://arxiv.org/abs/2403.13793)**  
  Phuong et al., 2024  
  *Summary:* Builds the first concrete evaluation suite for dangerous capabilities in frontier models across persuasion, cyber-offense, self-proliferation, and self-reasoning. Finds no strongly dangerous capabilities yet but identifies early warning signs.



#### 2023

- **[Artificial intelligence and biological misuse: Differentiating risks of language models and biological design tools](https://arxiv.org/abs/2306.13952)**  
  Sandbrink, 2023  
  *Summary:* Distinguishes the biosecurity risk profile of language models, which lower barriers to existing pathogen information, from biological design tools, which could enable novel agents. Argues the two need different governance.


- **[Can large language models democratize access to dual-use biotechnology?](https://arxiv.org/abs/2306.03809)**  
  Soice et al., 2023  
  *Summary:* Non-scientist students probed chatbots for guidance on obtaining pandemic-capable pathogens. The chatbots suggested candidate agents and pointed toward vendors unlikely to screen orders, demonstrating a concrete uplift risk.


- **[Generative Language Models and Automated Influence Operations: Emerging Threats and Potential Mitigations](https://arxiv.org/abs/2301.04246)**  
  Goldstein et al., 2023  
  *Summary:* Analyzes how generative models could change the actors, behaviors, and content of influence operations, lowering costs for propaganda generation and personalization. Proposes mitigations across model design, platforms, and access.



#### 2022

- **[Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://arxiv.org/abs/2209.07858)**  
  Ganguli et al., 2022  
  *Summary:* Crowdworkers red-teamed models of varying size and RLHF training, producing tens of thousands of adversarial conversations. Releases the dataset and analyzes how attack success scales with model size and safety training.


- **[Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)**  
  Perez et al., 2022  
  *Summary:* Uses one language model to automatically generate adversarial test cases that elicit harmful behavior from a target model, then classifies the outputs. Surfaces offensive content and data leakage far more cheaply than human red-teaming.


- **[Structured access: an emerging paradigm for safe AI deployment](https://arxiv.org/abs/2201.05159)**  
  Shevlane, 2022  
  *Summary:* Argues against a binary open-versus-closed release framing, proposing structured access where models are deployed as controllable services with usage restrictions, monitoring, and staged access.



#### 2020

- **[DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection](https://arxiv.org/abs/2001.00179)**  
  Tolosana et al., 2020  
  *Summary:* Surveys four categories of face manipulation including identity swap and entire face synthesis, alongside the public datasets and detection methods used to evaluate them.



#### 2019

- **[Defending Against Neural Fake News](https://arxiv.org/abs/1905.12616)**  
  Zellers et al., 2019  
  *Summary:* Introduces Grover, which generates controllable propaganda-style fake news that humans find more persuasive than human-written propaganda, and shows the same model is the best available detector of its own output.



#### 2018

- **[The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation](https://arxiv.org/abs/1802.07228)**  
  Brundage et al., 2018  
  *Summary:* A multi-institution report mapping how AI expands threats across digital, physical, and political security, including spear-phishing automation and surveillance-driven manipulation. Proposes prevention, response, and norm-setting.



