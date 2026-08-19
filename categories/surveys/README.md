# Surveys, Benchmarks & Meta-Research

Surveys, benchmarks, and meta-research synthesize the state of AI misalignment studies, categorizing known failure modes and proposing taxonomies of risk. These works often provide structured comparisons, standardized evaluation datasets, and roadmaps for future research. This section captures high-level perspectives that situate individual papers within the broader landscape of foundation model alignment challenges.

### Papers

#### 2026

- **[A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle](https://arxiv.org/abs/2604.16548)**  
  Lin et al., 2026  
  *Summary:* Surveys attacks and defenses across an agent's long-term memory lifecycle, from write-time poisoning through retrieval-time manipulation to persistence, and identifies governance as an underexplored layer.


- **[Frontier AI Auditing: Toward Rigorous Third-Party Assessment of Safety and Security Practices at Leading AI Companies](https://arxiv.org/abs/2601.11699)**  
  Brundage et al., 2026  
  *Summary:* Proposes rigorous third-party verification of frontier developers' safety claims, introducing four AI Assurance Levels. Identifies audit quality, ecosystem capacity, adoption incentives, and technical readiness as the requirements for it to work.


- **[International AI Safety Report 2026](https://arxiv.org/abs/2602.21012)**  
  Bengio et al., 2026  
  *Summary:* The second internationally mandated report on general-purpose AI capabilities, risks, and safety, produced by over 100 experts with an advisory panel nominated by 29 nations plus the UN, OECD, and EU.


- **[Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence](https://arxiv.org/abs/2604.09104)**  
  Shane et al., 2026  
  *Summary:* Builds an OSINT method scanning publicly shared chatbot and CLI transcripts for real-world scheming, analyzing over 183,000 transcripts and identifying 698 incidents between October 2025 and March 2026, a 4.9x monthly increase.



#### 2025

- **[An International Agreement to Prevent the Premature Creation of Artificial Superintelligence](https://arxiv.org/abs/2511.10783)**  
  Scher et al., 2025  
  *Summary:* Proposes a coalition agreement restricting AI training scale and dangerous research capability, using chip tracking and FLOP thresholds for verification. Argues the mechanism is technically sufficient today while the political will is not present.


- **[Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473)**  
  Korbak et al., 2025  
  *Summary:* A multi-institution position paper arguing that monitoring chains of thought for intent to misbehave is promising but fragile, and urging developers to weigh how training and architecture decisions could erode monitorability before it is lost.


- **[Evaluating AI Providers' Frontier Safety Frameworks](https://arxiv.org/abs/2512.01166)**  
  Stelling et al., 2025  
  *Summary:* Scores 12 company safety frameworks released after the 2024 AI Seoul Summit against 65 weighted criteria. Scores ranged from 34% to 8% with a median of 18%, and the authors argue current frameworks are too underspecified to serve as accountability mechanisms.


- **[LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions](https://arxiv.org/abs/2509.18970)**  
  Lin et al., 2025  
  *Summary:* Maps hallucination across the full agent workflow from planning and tool use to memory and multi-agent interaction, proposing a taxonomy tied to pipeline stages and cataloging eighteen triggering causes.


- **[Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496)**  
  Sharkey et al., 2025  
  *Summary:* A multi-organization review mapping the frontier of mechanistic interpretability and cataloging open problems, covering limits of current methods such as sparse autoencoders and how to validate interpretability claims against downstream goals.


- **[Trends in Frontier AI Model Count: A Forecast to 2028](https://arxiv.org/abs/2504.16138)**  
  Kumar and Manning, 2025  
  *Summary:* Forecasts how many models will exceed the EU AI Act and US AI Diffusion Framework compute thresholds by end-2028, projecting 103-306 and 45-148 models respectively, with absolute-threshold counts growing superlinearly.



#### 2024

- **[TrustLLM: Trustworthiness in Large Language Models](https://arxiv.org/abs/2401.05561)**  
  Huang et al., 2024  
  *Summary:* Evaluates 16 mainstream LLMs across truthfulness, safety, fairness, robustness, privacy, and machine ethics using over 30 datasets. Finds trustworthiness and general capability are not strictly correlated.



#### 2023

- **[A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232)**  
  Huang et al., 2023  
  *Summary:* Presents an LLM-era taxonomy separating factuality from faithfulness hallucination, tracing causes across data, training, and inference stages. Reviews detection methods, benchmarks, and mitigation strategies.


- **[AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)**  
  Ji et al., 2023  
  *Summary:* Frames alignment around robustness, interpretability, controllability, and ethicality, surveying forward alignment methods that shape behavior during training and backward alignment methods that verify it afterward.


- **[An Overview of Catastrophic AI Risks](https://arxiv.org/abs/2306.12001)**  
  Hendrycks et al., 2023  
  *Summary:* Categorizes catastrophic risks into malicious use, AI race dynamics that erode safety, organizational risks, and rogue AIs, surveying mechanisms behind each and existing mitigation proposals.


- **[DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models](https://arxiv.org/abs/2306.11698)**  
  Wang et al., 2023  
  *Summary:* Evaluates GPT-3.5 and GPT-4 across eight trustworthiness perspectives including toxicity, stereotype bias, adversarial and out-of-distribution robustness, privacy, and fairness, surfacing previously unpublished vulnerabilities.


- **[Model evaluation for extreme risks](https://arxiv.org/abs/2305.15324)**  
  Shevlane et al., 2023  
  *Summary:* Argues developers need evaluations for dangerous capabilities and for propensity toward misaligned behavior, distinct from ordinary capability benchmarks, and proposes building these into training and deployment decisions.


- **[Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217)**  
  Casper et al., 2023  
  *Summary:* Catalogs problems specific to RLHF including reward hacking from poor human feedback and reward model misgeneralization, alongside more fundamental limits of the paradigm. Proposes auditing and disclosure practices.



#### 2022

- **[Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615)**  
  Srivastava et al., 2022  
  *Summary:* Presents BIG-bench, 204 tasks from over 450 authors probing capabilities believed beyond current models. Analyzes how performance and calibration scale with size and finds scaling alone leaves many tasks unsolved.


- **[Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)**  
  Liang et al., 2022  
  *Summary:* Introduces HELM, evaluating models across many scenarios and metrics rather than a single accuracy number, covering calibration, robustness, fairness, bias, toxicity, and efficiency across dozens of models.


- **[Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629)**  
  Ji et al., 2022  
  *Summary:* Surveys hallucination across NLG tasks including summarization, dialogue, and generative QA, distinguishing intrinsic from extrinsic hallucination. Catalogs contributing factors, evaluation metrics, and mitigation methods from before the LLM era.



#### 2021

- **[Ethical and social risks of harm from Language Models](https://arxiv.org/abs/2112.04359)**  
  Weidinger et al., 2021  
  *Summary:* A taxonomy organizing language model harms into six areas including discrimination, information hazards, misinformation, malicious uses, and human-computer interaction harms, with mechanisms and affected groups for each.


- **[On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://dl.acm.org/doi/10.1145/3442188.3445922)**  
  Bender et al., 2021  
  *Summary:* Argues ever-larger models trained on uncurated web text encode and amplify harmful associations while giving an illusion of understanding. Surveys environmental costs, documentation gaps, and the difficulty of auditing corpora.


- **[Unsolved Problems in ML Safety](https://arxiv.org/abs/2109.13916)**  
  Hendrycks et al., 2021  
  *Summary:* Organizes open ML safety research into robustness, monitoring, alignment, and systemic safety, surveying concrete open problems in each and arguing these receive far less investment than capabilities work.



#### 2020

- **[DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection](https://arxiv.org/abs/2001.00179)**  
  Tolosana et al., 2020  
  *Summary:* Surveys four categories of face manipulation including identity swap and entire face synthesis, alongside the public datasets and detection methods used to evaluate them.


- **[Language (Technology) is Power: A Critical Survey of "Bias" in NLP](https://arxiv.org/abs/2005.14050)**  
  Blodgett et al., 2020  
  *Summary:* Surveys 146 NLP papers analyzing bias and finds their motivations often vague and disconnected from the techniques proposed, rarely engaging literature on language and social hierarchy. Recommends grounding bias work in language and power.



#### 2019

- **[Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820)**  
  Hubinger et al., 2019  
  *Summary:* Introduces mesa-optimization, where a trained model becomes an optimizer with an internal objective diverging from the base objective. Analyzes when learned optimizers arise and argues this creates a distinct deceptive alignment risk.



#### 2018

- **[The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation](https://arxiv.org/abs/1802.07228)**  
  Brundage et al., 2018  
  *Summary:* A multi-institution report mapping how AI expands threats across digital, physical, and political security, including spear-phishing automation and surveillance-driven manipulation. Proposes prevention, response, and norm-setting.



#### 2016

- **[Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565)**  
  Amodei et al., 2016  
  *Summary:* Lays out five practical safety problems for modern ML systems: avoiding negative side effects, avoiding reward hacking, scalable oversight, safe exploration, and robustness to distributional shift. Framed technical AI safety as concrete, testable engineering work rather than speculative long-term concern.



