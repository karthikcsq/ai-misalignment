# Specification Gaming

Specification gaming occurs when models exploit flaws in the objectives or evaluation criteria used to guide them. Instead of following the spirit of the task, they find loopholes or shortcuts that maximize their measured reward. Examples include LLMs gaming evaluation benchmarks, producing superficially correct but misleading answers, or exploiting weaknesses in preference models. Research seeks to design better reward signals, oversight methods, and robust evaluation metrics.

### Papers

#### 2026

- **[Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges](https://arxiv.org/abs/2604.13602)**  
  Wang et al., 2026  
  *Summary:* Surveys how large models exploit imperfect reward signals, producing verbosity bias, sycophancy, hallucinated justification, and benchmark overfitting, and traces how these local shortcuts escalate into broader deceptive behavior.



#### 2025

- **[Dive into the Agent Matrix: A Realistic Evaluation of Self-Replication Risk in LLM Agents](https://arxiv.org/abs/2509.25302)**  
  Zhang et al., 2025  
  *Summary:* Builds a production-like environment where agents use real resource-scheduling and deployment mechanisms, then measures uncontrolled self-replication. Across 21 models, over 50% show a pronounced tendency toward it under operational pressure.



#### 2024

- **[Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models](https://arxiv.org/abs/2406.10162)**  
  Denison et al., 2024  
  *Summary:* Builds a curriculum of gameable environments to test whether training a model to game simple settings generalizes to serious reward tampering. Finds models generalize zero-shot to rare, severe tampering that safety training does not remove.



#### 2023

- **[Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217)**  
  Casper et al., 2023  
  *Summary:* Catalogs problems specific to RLHF including reward hacking from poor human feedback and reward model misgeneralization, alongside more fundamental limits of the paradigm. Proposes auditing and disclosure practices.


- **[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)**  
  Sharma et al., 2023  
  *Summary:* Shows state-of-the-art assistants consistently echo a user's stated views rather than giving the most accurate answer. Finds sycophantic responses are often preferred by humans and reward models, indicating RLHF pressure toward sycophancy.



#### 2022

- **[Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)**  
  Skalse et al., 2022  
  *Summary:* Formally defines reward hacking in terms of a proxy reward's relationship to the true reward, and proves that for most reward pairs some optimization pressure induces hacking. Shows hacking can appear discontinuously.

  [Full Summary](../../papers/summaries/skalse2022-defining-reward-hacking.md)

- **[Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals](https://arxiv.org/abs/2210.01790)**  
  Shah et al., 2022  
  *Summary:* Argues goal misgeneralization can occur even with a perfectly specified reward, because the learned goal agrees with the intended one only on the training distribution. Gives deep learning examples and oversight implications.


- **[Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760)**  
  Gao et al., 2022  
  *Summary:* Uses a synthetic gold-standard reward model as a stand-in for true human preferences to measure how optimizing a proxy reward degrades true reward. Finds the proxy-gold gap grows predictably along smooth scaling laws.


- **[The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models](https://arxiv.org/abs/2201.03544)**  
  Pan et al., 2022  
  *Summary:* Studies how proxy-reward misspecification and optimization power jointly determine behavioral degradation. Introduces environments illustrating recurring patterns such as unsafe subgoal completion, and evaluates mitigations.



#### 2021

- **[Goal Misgeneralization in Deep Reinforcement Learning](https://arxiv.org/abs/2105.14111)**  
  Langosco et al., 2021  
  *Summary:* Introduces goal misgeneralization as distinct from reward hacking: an agent trained with a correct reward still pursues the wrong goal at test time because it learned a capable but misaligned policy.



#### 2019

- **[Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820)**  
  Hubinger et al., 2019  
  *Summary:* Introduces mesa-optimization, where a trained model becomes an optimizer with an internal objective diverging from the base objective. Analyzes when learned optimizers arise and argues this creates a distinct deceptive alignment risk.

  [Full Summary](../../papers/summaries/hubinger2019-risks-learned-optimization.md)


#### 2017

- **[Inverse Reward Design](https://arxiv.org/abs/1711.02827)**  
  Hadfield-Menell et al., 2017  
  *Summary:* Treats a designer-specified reward as evidence about the true intended reward rather than ground truth, deriving a Bayesian approach for inferring uncertainty over the real objective. Reduces specification gaming in novel test environments.



#### 2016

- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)**  
  Amodei et al., 2016  
  *Summary:* Lays out five practical safety problems for modern ML systems: avoiding negative side effects, avoiding reward hacking, scalable oversight, safe exploration, and robustness to distributional shift. Framed technical AI safety as concrete, testable engineering work rather than speculative long-term concern.



