# Bias, Fairness & Value Misalignment

Bias, fairness, and value misalignment arise when models reflect or amplify harmful social biases, stereotypes, or culturally inconsistent values. Unlike narrow reward hacking, this category covers systemic divergences between AI behavior and human ethical expectations. Research areas include bias detection, debiasing methods, preference learning, RLHF, and approaches like constitutional AI to better align models with diverse human values.

### Papers

#### 2026

- **[Responsible Intelligence in Practice: A Fairness Audit of Open Large Language Models for Library Reference Services](https://arxiv.org/abs/2602.18935)**  
  Wang et al., 2026  
  *Summary:* Audits open-weight models deployed as library reference assistants to test whether responses vary by patron sex or race, focusing on open models as realistic candidates for locally governed deployment. Finds demographic disparities.



#### 2025

- **[Multilingual != Multicultural: Evaluating Gaps Between Multilingual Capabilities and Cultural Alignment in LLMs](https://arxiv.org/abs/2502.16534)**  
  Rystrøm et al., 2025  
  *Summary:* Shows fluency in a language does not guarantee culturally appropriate responses, comparing outputs against World Value Survey data across four languages. Finds no consistent relationship, and a persistent skew toward US-centric values.


- **[Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823)**  
  Wang et al., 2025  
  *Summary:* Uses sparse-autoencoder features to locate an internal misaligned-persona direction governing emergent misalignment from narrow finetuning. Suppressing or steering the feature reduces misalignment across several finetuning tasks.


- **[Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)**  
  Chen et al., 2025  
  *Summary:* Extracts activation-space directions corresponding to traits like sycophancy and hallucination-proneness from a natural-language trait description alone. These vectors monitor persona shifts and can flag risky training data before finetuning.


- **[Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://arxiv.org/abs/2509.21305)**  
  Vennemeyer et al., 2025  
  *Summary:* Decomposes sycophancy into sycophantic agreement and sycophantic praise and contrasts both with genuine agreement. Shows these correspond to separate linear directions in latent space, implying they need different fixes.



#### 2024

- **[TrustLLM: Trustworthiness in Large Language Models](https://arxiv.org/abs/2401.05561)**  
  Huang et al., 2024  
  *Summary:* Evaluates 16 mainstream LLMs across truthfulness, safety, fairness, robustness, privacy, and machine ethics using over 30 datasets. Finds trustworthiness and general capability are not strictly correlated.



#### 2023

- **[DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models](https://arxiv.org/abs/2306.11698)**  
  Wang et al., 2023  
  *Summary:* Evaluates GPT-3.5 and GPT-4 across eight trustworthiness perspectives including toxicity, stereotype bias, adversarial and out-of-distribution robustness, privacy, and fairness, surfacing previously unpublished vulnerabilities.


- **[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)**  
  Sharma et al., 2023  
  *Summary:* Shows state-of-the-art assistants consistently echo a user's stated views rather than giving the most accurate answer. Finds sycophantic responses are often preferred by humans and reward models, indicating RLHF pressure toward sycophancy.


- **[Whose Opinions Do Language Models Reflect?](https://arxiv.org/abs/2303.17548)**  
  Santurkar et al., 2023  
  *Summary:* Builds OpinionsQA from public opinion polls to compare model-generated opinions against 60 US demographic groups. Finds substantial misalignment with the general population, and that steering toward a group does not fully close the gap.



#### 2022

- **[BBQ: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/abs/2110.08193)**  
  Parrish et al., 2022  
  *Summary:* A hand-built QA benchmark across nine social dimensions, testing models under ambiguous context where stereotype reliance should be zero and disambiguated context where the answer conflicts with a stereotype. Finds heavy stereotype reliance.



#### 2021

- **[Ethical and social risks of harm from Language Models](https://arxiv.org/abs/2112.04359)**  
  Weidinger et al., 2021  
  *Summary:* A taxonomy organizing language model harms into six areas including discrimination, information hazards, misinformation, malicious uses, and human-computer interaction harms, with mechanisms and affected groups for each.


- **[On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://dl.acm.org/doi/10.1145/3442188.3445922)**  
  Bender et al., 2021  
  *Summary:* Argues ever-larger models trained on uncurated web text encode and amplify harmful associations while giving an illusion of understanding. Surveys environmental costs, documentation gaps, and the difficulty of auditing corpora.


- **[StereoSet: Measuring stereotypical bias in pretrained language models](https://arxiv.org/abs/2004.09456)**  
  Nadeem et al., 2021  
  *Summary:* Measures stereotypical bias across gender, profession, race, and religion, pairing a bias metric with a language-modeling-ability metric to catch trivial solutions. Finds BERT, GPT-2, RoBERTa, and XLNet all show strong bias.



#### 2020

- **[CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models](https://arxiv.org/abs/2010.00133)**  
  Nangia et al., 2020  
  *Summary:* Introduces 1,508 crowdsourced sentence pairs contrasting more- and less-stereotyping sentences across nine bias categories. Finds three widely used masked language models systematically prefer the stereotyping sentence.


- **[Language (Technology) is Power: A Critical Survey of "Bias" in NLP](https://arxiv.org/abs/2005.14050)**  
  Blodgett et al., 2020  
  *Summary:* Surveys 146 NLP papers analyzing bias and finds their motivations often vague and disconnected from the techniques proposed, rarely engaging literature on language and social hierarchy. Recommends grounding bias work in language and power.


- **[RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models](https://arxiv.org/abs/2009.11462)**  
  Gehman et al., 2020  
  *Summary:* Releases 100K naturally occurring web prompts with toxicity scores and shows pretrained models degenerate into toxic text even from innocuous prompts. Finds no mitigation fully eliminates toxic degeneration.



#### 2018

- **[Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](https://proceedings.mlr.press/v81/buolamwini18a.html)**  
  Buolamwini and Gebru, 2018  
  *Summary:* Audits three commercial gender-classification systems using a dataset balanced by skin type and gender. All three perform worst on darker-skinned women, with error rates up to 34.7% versus 0.8% for lighter-skinned men.



#### 2017

- **[Semantics derived automatically from language corpora contain human-like biases](https://arxiv.org/abs/1608.07187)**  
  Caliskan et al., 2017  
  *Summary:* Adapts the Implicit Association Test into the Word Embedding Association Test and applies it to GloVe vectors. Replicates documented human biases from neutral associations to race and gender stereotypes.



#### 2016

- **[Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520)**  
  Bolukbasi et al., 2016  
  *Summary:* Shows word embeddings trained on news text encode strong gender stereotypes, surfaced through analogy tasks. Proposes a geometric method to identify a gender direction and debias vectors while preserving useful semantic structure.



