# Hallucination

Hallucination refers to cases where large language models generate text that is factually incorrect, logically inconsistent, or entirely fabricated. These errors undermine trust in high-stakes settings such as scientific writing, healthcare, and legal contexts. Research focuses on understanding sources of hallucination, building benchmarks to measure it, and developing mitigation strategies through retrieval augmentation, improved training data, and alignment techniques.

### Papers

#### 2026

- **[Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation](https://arxiv.org/abs/2606.04435)**  
  Mishra, 2026  
  *Summary:* Defines cascading hallucination as a distinct failure mode in multi-step agentic retrieval, where an early error propagates and amplifies through later reasoning into a confident wrong answer, and proposes a framework to detect and mitigate it.


- **[Streaming Hallucination Detection in Long Chain-of-Thought Reasoning](https://arxiv.org/abs/2601.02170)**  
  Lu et al., 2026  
  *Summary:* Treats hallucination in long chain-of-thought reasoning as an evolving latent state rather than isolated errors, introducing a streaming method that tracks per-step judgments to detect hallucination during generation.



#### 2025

- **[Auditing Meta-Cognitive Hallucinations in Reasoning Large Language Models](https://arxiv.org/abs/2505.13143)**  
  Lu et al., 2025  
  *Summary:* Studies how reasoning models reinforce their own errors through flawed reflective reasoning, producing confident hallucinated conclusions. Introduces black-box auditing that locates where in a reasoning chain a hallucination originates.


- **[LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions](https://arxiv.org/abs/2509.18970)**  
  Lin et al., 2025  
  *Summary:* Maps hallucination across the full agent workflow from planning and tool use to memory and multi-agent interaction, proposing a taxonomy tied to pipeline stages and cataloging eighteen triggering causes.


- **[SEReDeEP: Hallucination Detection in Retrieval-Augmented Models via Semantic Entropy and Context-Parameter Fusion](https://arxiv.org/abs/2505.07528)**  
  Wang, 2025  
  *Summary:* Argues RAG hallucinations stem from an imbalance between retrieved context and internal parametric knowledge, adding semantic entropy signals to context-parameter fusion scoring to improve detection.


- **[Semantic Energy: Detecting LLM Hallucination Beyond Entropy](https://arxiv.org/abs/2508.14496)**  
  Ma et al., 2025  
  *Summary:* Identifies that semantic entropy relies on post-softmax probabilities and misses inherent model uncertainty. Proposes Semantic Energy, operating on penultimate-layer logits with semantic clustering and an energy distribution.


- **[Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)**  
  Kalai et al., 2025  
  *Summary:* Argues hallucinations arise statistically from next-token prediction and are compounded by evaluations that score like standardized tests, rewarding a confident guess over admitting uncertainty. Proposes crediting calibrated uncertainty in mainstream benchmarks.



#### 2023

- **[A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232)**  
  Huang et al., 2023  
  *Summary:* Presents an LLM-era taxonomy separating factuality from faithfulness hallucination, tracing causes across data, training, and inference stages. Reviews detection methods, benchmarks, and mitigation strategies.


- **[FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251)**  
  Min et al., 2023  
  *Summary:* Breaks long-form generations into atomic facts and scores the percentage supported by a trusted knowledge source. Evaluates several commercial LLMs and provides a cheaper automated estimator approximating human judgments.


- **[HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models](https://arxiv.org/abs/2305.11747)**  
  Li et al., 2023  
  *Summary:* Constructs a 35,000-sample benchmark of generated and human-annotated hallucinated examples across QA, dialogue, and summarization. Finds LLMs struggle to recognize hallucinated content, and that external knowledge or reasoning steps improve recognition.


- **[How Language Model Hallucinations Can Snowball](https://arxiv.org/abs/2305.13534)**  
  Zhang et al., 2023  
  *Summary:* Shows that once a model commits to an early false claim it generates further false claims to justify the first, even when it can identify those later claims as wrong if asked directly. Demonstrates the effect across primality, US senators, and multi-hop reasoning questions.


- **[SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://arxiv.org/abs/2303.08896)**  
  Manakul et al., 2023  
  *Summary:* Detects hallucinated content without external knowledge bases or model internals by sampling multiple responses to the same prompt and measuring consistency between them. Shows inconsistent sampled answers correlate strongly with factually unsupported statements.


- **[Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664)**  
  Kuhn et al., 2023  
  *Summary:* Introduces semantic entropy, clustering sampled generations by meaning via bidirectional entailment before computing entropy. Shows this predicts hallucinated, low-confidence answers better than token-level likelihood.



#### 2022

- **[Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)**  
  Kadavath et al., 2022  
  *Summary:* Studies whether models can predict which questions they will answer correctly, via calibrated probabilities and a self-evaluation "P(True)" approach where the model judges its own prior answers. Finds self-evaluation calibration improves with model size and few-shot prompting.


- **[Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629)**  
  Ji et al., 2022  
  *Summary:* Surveys hallucination across NLG tasks including summarization, dialogue, and generative QA, distinguishing intrinsic from extrinsic hallucination. Catalogs contributing factors, evaluation metrics, and mitigation methods from before the LLM era.



#### 2021

- **[TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958)**  
  Lin et al., 2021  
  *Summary:* Introduces an 817-question benchmark across 38 categories testing whether models generate falsehoods that mimic common human misconceptions. Found larger models were often less truthful than smaller ones, since scaling amplifies imitation of training-data falsehoods rather than correcting them.



#### 2020

- **[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)**  
  Lewis et al., 2020  
  *Summary:* Introduces RAG, combining a pretrained seq2seq generator with a dense retriever over Wikipedia passages and training both jointly. Set state of the art on open-domain QA and became the foundational architecture for retrieval-based hallucination mitigation.



