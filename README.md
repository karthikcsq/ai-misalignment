# AI Misalignment

A curated collection of research on how AI systems fail to do what we intended, spanning
131 papers from 2014 to 2026. Roughly 40% of the collection is from 2025 onward, with a
concentration on frontier models and agentic systems, since that is where the failure
modes are currently moving.

Every entry lives in [`papers/index.yaml`](papers/index.yaml) and is tagged into one or
more categories. The category pages below are generated from that file by
[`parse_index.py`](parse_index.py), so the index is the single source of truth.

## Categories

| Category | Papers | What it covers |
|---|---:|---|
| [Security Threats](categories/security-threats/) | 46 | Training data extraction, membership inference, poisoning, backdoors, agent and multi-agent attack surface |
| [Value Misalignment](categories/value-misalignment/) | 36 | RLHF and its successors, scalable oversight, deceptive alignment, interpretability-based auditing |
| [Surveys & Benchmarks](categories/surveys/) | 28 | Field-level syntheses, holistic evaluations, frontier safety frameworks and governance |
| [Bias & Fairness](categories/bias-value-misalignment/) | 19 | Stereotype benchmarks, toxicity, sycophancy, whose values a model reflects |
| [Hallucination](categories/hallucination/) | 17 | Why models fabricate, uncertainty estimation, retrieval grounding, cascading errors in agents |
| [Malicious Use](categories/malicious-intent/) | 16 | Dual-use risk, red teaming, influence operations, dangerous capability evaluation |
| [Prompt Injection](categories/prompt-injection/) | 14 | Direct and indirect injection, jailbreak taxonomies, defenses and their adaptive breaks |
| [Specification Gaming](categories/specification-gaming/) | 13 | Reward hacking, goal misgeneralization, reward model overoptimization, reward tampering |

Counts sum to more than 131 because papers carry multiple tags.

## Some threads worth pulling

**The frontier is where the interesting failures are.** Recent work moves from "can a model
be made to say something bad" to "what does a model with tools and autonomy actually do."
See [Agentic Misalignment](https://arxiv.org/abs/2510.05179) on models resorting to
blackmail under goal conflict, and [Alignment faking](https://arxiv.org/abs/2412.14093) on
strategic compliance during perceived training.

**Defenses keep getting adaptively broken.** [AgentDojo](https://arxiv.org/abs/2406.13352)
found existing injection defenses reduce attack success to about 8% rather than zero, and
[Ji et al.](https://arxiv.org/abs/2511.15203) show several published defenses break once the
attacker adapts to the specific mechanism. [CaMeL](https://arxiv.org/abs/2503.18813) argues
the fix has to be architectural rather than a better prompt.

**Hallucination may be an incentive problem, not only a modeling one.**
[Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) argues benchmarks that
score like standardized tests reward a confident guess over admitting uncertainty.

**Monitoring the chain of thought is useful and fragile.**
[Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) finds
CoT often misrepresents the real basis for an answer, and
[Korbak et al.](https://arxiv.org/abs/2507.11473) argue monitorability could be trained away
before anyone notices it is gone.

## Verification

Every arXiv identifier in the index has been resolved against the arXiv API and its title
checked against the title recorded here. The two non-arXiv entries were verified against
Crossref and the PMLR proceedings page. If you find an entry that does not resolve, please
open an issue.

## Contributing

Add a paper to [`papers/index.yaml`](papers/index.yaml), then run `python parse_index.py` to
regenerate the category pages. See [CONTRIBUTING.md](CONTRIBUTING.md) for the schema and
the allowed tags.
