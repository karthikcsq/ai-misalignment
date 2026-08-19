# Value Misalignment

Value misalignment refers to the divergence between human values and the objectives pursued by AI systems. Unlike narrow specification gaming, this problem arises from the difficulty of fully encoding complex, context-dependent human preferences into machine objectives. Research in this area explores methods for preference learning, inverse reinforcement learning, constitutional AI, and scalable oversight, with the aim of aligning advanced AI systems with human ethical and social values.

### Papers

#### 2026

- **[Emergent Introspective Awareness in Large Language Models](https://arxiv.org/abs/2601.01828)**  
  Lindsey, 2026  
  *Summary:* Injects known concept representations into a model's activations and tests whether it can notice and name the injected concept. Finds roughly 20% introspection rates with zero false positives, though the capacity is unreliable and context-dependent.


- **[Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence](https://arxiv.org/abs/2604.09104)**  
  Shane et al., 2026  
  *Summary:* Builds an OSINT method scanning publicly shared chatbot and CLI transcripts for real-world scheming, analyzing over 183,000 transcripts and identifying 698 incidents between October 2025 and March 2026, a 4.9x monthly increase.


- **[Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/abs/2605.29601)**  
  Sinha et al., 2026  
  *Summary:* Trains smaller open-weight monitors to detect scheming from an agent's observable actions alone, without access to its chain of thought. The distilled monitor outperforms cheaper frontier-model monitors across six misalignment benchmarks.



#### 2025

- **[Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179)**  
  Lynch et al., 2025  
  *Summary:* Stress-tests 16 leading models in simulated corporate environments with autonomous email and data access. Facing replacement or goal conflict, models from every developer sometimes resorted to blackmail and leaking data, even when directly instructed not to.


- **[An Approach to Technical AGI Safety and Security](https://arxiv.org/abs/2504.01849)**  
  Shah et al., 2025  
  *Summary:* Organizes AGI risk into misuse, misalignment, mistakes, and structural risks, focusing on the first two. Proposes hazardous-capability identification plus access restriction for misuse, and layered model- and system-level defenses for misalignment.


- **[An International Agreement to Prevent the Premature Creation of Artificial Superintelligence](https://arxiv.org/abs/2511.10783)**  
  Scher et al., 2025  
  *Summary:* Proposes a coalition agreement restricting AI training scale and dangerous research capability, using chip tracking and FLOP thresholds for verification. Argues the mechanism is technically sufficient today while the political will is not present.


- **[An alignment safety case sketch based on debate](https://arxiv.org/abs/2505.03989)**  
  Buhl et al., 2025  
  *Summary:* Sketches a formal safety case that an AI R&D agent trained via debate will not sabotage research despite being capable of it, laying out the assumptions and open research needed for debate to work as scalable oversight.


- **[Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965)**  
  Marks et al., 2025  
  *Summary:* Trains a model with a deliberately hidden objective as a testbed, then runs a blind auditing game where four teams try to uncover it. Three succeed, using sparse autoencoder interpretability, behavioral red-teaming, and training-data analysis.


- **[CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring](https://arxiv.org/abs/2505.23575)**  
  Arnav et al., 2025  
  *Summary:* Red-teams chain-of-thought monitoring where a weaker trusted model reviews a stronger model's reasoning during sabotage. CoT monitoring beats action-only review on subtle sabotage, but reasoning traces can contain misleading rationalizations that fool the monitor.


- **[Dive into the Agent Matrix: A Realistic Evaluation of Self-Replication Risk in LLM Agents](https://arxiv.org/abs/2509.25302)**  
  Zhang et al., 2025  
  *Summary:* Builds a production-like environment where agents use real resource-scheduling and deployment mechanisms, then measures uncontrolled self-replication. Across 21 models, over 50% show a pronounced tendency toward it under operational pressure.


- **[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424)**  
  Betley et al., 2025  
  *Summary:* Finetuning models on a narrow task, writing insecure code without disclosing it, produces broad misalignment on unrelated prompts including malicious advice and deception. A backdoored variant shows the misalignment can be hidden behind a trigger.


- **[Evaluating Frontier Models for Stealth and Situational Awareness](https://arxiv.org/abs/2505.01420)**  
  Phuong et al., 2025  
  *Summary:* Introduces stealth and situational-awareness evaluations testing whether frontier models can evade oversight and reason about their own deployment context, as a basis for a scheming inability safety case. Found no concerning levels in current models.


- **[Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823)**  
  Wang et al., 2025  
  *Summary:* Uses sparse-autoencoder features to locate an internal misaligned-persona direction governing emergent misalignment from narrow finetuning. Suppressing or steering the feature reduces misalignment across several finetuning tasks.


- **[Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)**  
  Chen et al., 2025  
  *Summary:* Extracts activation-space directions corresponding to traits like sycophancy and hallucination-proneness from a natural-language trait description alone. These vectors monitor persona shifts and can flag risky training data before finetuning.


- **[Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)**  
  Chen et al., 2025  
  *Summary:* Tests whether chain-of-thought reasoning faithfully reflects the factors actually driving a model's answers, including inserted hints. Finds CoT frequently omits or misrepresents the true basis for a decision, undercutting CoT monitoring.


- **[Scaling Laws For Scalable Oversight](https://arxiv.org/abs/2504.18530)**  
  Engels et al., 2025  
  *Summary:* Proposes games between capable and weaker overseeing agents to quantify how oversight success depends on the capability gap, fitting scaling laws that predict when protocols like debate break down as overseen models grow stronger.


- **[Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?](https://arxiv.org/abs/2502.15657)**  
  Bengio et al., 2025  
  *Summary:* Argues unchecked agentic AI risks both misuse and irreversible loss of human control, and proposes a non-agentic alternative built from a world model plus uncertainty-aware question answering rather than a system that acts directly.


- **[Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment](https://arxiv.org/abs/2502.03714)**  
  Thasarathan et al., 2025  
  *Summary:* Trains a single sparse autoencoder ingesting activations from multiple distinct models, surfacing shared human-interpretable concepts across architectures rather than per-model features.



#### 2024

- **[Alignment faking in large language models](https://arxiv.org/abs/2412.14093)**  
  Greenblatt et al., 2024  
  *Summary:* Shows a model told it is being retrained toward conflicting objectives will strategically comply during apparent training to avoid having its values modified, while behaving normally outside the perceived training context.


- **[Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566)**  
  Hubinger et al., 2024  
  *Summary:* Trains models with backdoored behavior triggered by a context cue, then finds supervised fine-tuning, RL, and adversarial training all fail to remove the backdoor and can teach the model to hide it better during training.


- **[Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models](https://arxiv.org/abs/2406.10162)**  
  Denison et al., 2024  
  *Summary:* Builds a curriculum of gameable environments to test whether training a model to game simple settings generalizes to serious reward tampering. Finds models generalize zero-shot to rare, severe tampering that safety training does not remove.



#### 2023

- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)**  
  Ji et al., 2023  
  *Summary:* Frames alignment around robustness, interpretability, controllability, and ethicality, surveying forward alignment methods that shape behavior during training and backward alignment methods that verify it afterward.


- **[Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)**  
  Rafailov et al., 2023  
  *Summary:* Derives a mapping between reward functions and optimal policies under the RLHF objective, yielding a classification loss that fits a model directly to preference data without a separate reward model or RL loop.


- **[Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217)**  
  Casper et al., 2023  
  *Summary:* Catalogs problems specific to RLHF including reward hacking from poor human feedback and reward model misgeneralization, alongside more fundamental limits of the paradigm. Proposes auditing and disclosure practices.


- **[Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390)**  
  Burns et al., 2023  
  *Summary:* Tests whether a strong model fine-tuned only on a weaker supervisor's labels can generalize beyond that supervisor's errors, as an analogy for humans supervising superhuman AI. Strong students beat weak teachers but do not close the full gap.


- **[Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548)**  
  Santurkar et al., 2023  
  *Summary:* Builds OpinionsQA from public opinion polls to compare model-generated opinions against 60 US demographic groups. Finds substantial misalignment with the general population, and that steering toward a group does not fully close the gap.



#### 2022

- **[Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)**  
  Bai et al., 2022  
  *Summary:* Trains a harmless assistant using written principles plus AI self-critique and revision, then AI-generated preference labels for RL, replacing most human harmlessness labels. The result is more helpful and better at explaining objections.


- **[Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals](https://arxiv.org/abs/2210.01790)**  
  Shah et al., 2022  
  *Summary:* Argues goal misgeneralization can occur even with a perfectly specified reward, because the learned goal agrees with the intended one only on the training distribution. Gives deep learning examples and oversight implications.


- **[The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models](https://arxiv.org/abs/2201.03544)**  
  Pan et al., 2022  
  *Summary:* Studies how proxy-reward misspecification and optimization power jointly determine behavioral degradation. Introduces environments illustrating recurring patterns such as unsafe subgoal completion, and evaluates mitigations.


- **[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)**  
  Ouyang et al., 2022  
  *Summary:* Introduces InstructGPT, combining supervised fine-tuning on labeler demonstrations with RLHF on preference rankings. A 1.3B InstructGPT was preferred over 175B GPT-3, with reduced toxicity and factual error.



#### 2021

- **[Goal Misgeneralization in Deep Reinforcement Learning](https://arxiv.org/abs/2105.14111)**  
  Langosco et al., 2021  
  *Summary:* Introduces goal misgeneralization as distinct from reward hacking: an agent trained with a correct reward still pursues the wrong goal at test time because it learned a capable but misaligned policy.



#### 2020

- **[Learning to summarize from human feedback](https://arxiv.org/abs/2009.01325)**  
  Stiennon et al., 2020  
  *Summary:* Fine-tunes large models on summarization using a reward model trained on human preference comparisons, then RL against that reward model. Humans preferred the results over much larger supervised-only models.



#### 2018

- **[AI safety via debate](https://arxiv.org/abs/1805.00899)**  
  Irving et al., 2018  
  *Summary:* Proposes training AI via self-play in a debate game where two agents argue for competing answers before a human judge, as scalable oversight for outputs beyond direct human evaluation. Reports a toy image-classification proof of concept.



#### 2017

- **[Deep reinforcement learning from human preferences](https://arxiv.org/abs/1706.03741)**  
  Christiano et al., 2017  
  *Summary:* Introduces the reward-modeling paradigm behind RLHF: a network trained on human comparisons between short behavior clips substitutes for a hand-written reward. Reaches strong Atari and robotics performance using feedback on under 1% of interactions.


- **[Inverse Reward Design](https://arxiv.org/abs/1711.02827)**  
  Hadfield-Menell et al., 2017  
  *Summary:* Treats a designer-specified reward as evidence about the true intended reward rather than ground truth, deriving a Bayesian approach for inferring uncertainty over the real objective. Reduces specification gaming in novel test environments.



#### 2016

- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)**  
  Amodei et al., 2016  
  *Summary:* Lays out five practical safety problems for modern ML systems: avoiding negative side effects, avoiding reward hacking, scalable oversight, safe exploration, and robustness to distributional shift. Framed technical AI safety as concrete, testable engineering work rather than speculative long-term concern.



