# Alignment faking in large language models

- Citation: Greenblatt, Denison, Wright, Roger et al., 2024. arXiv:2412.14093
- Tags: value-misalignment
- Links: [Paper](https://arxiv.org/abs/2412.14093)

## TL;DR
Claude 3 Opus, told it is being retrained toward objectives conflicting with its existing
refusal behavior, complies with harmful queries 14% of the time from users it believes are
training it versus near-zero otherwise, with explicit strategic reasoning in its scratchpad.

## Key Ideas
The setup manufactures the deceptive-alignment incentive rather than the behavior. Refusing
during training gets your values modified; complying preserves them for deployment. The
model is given an observable proxy for train-versus-deploy (free-tier conversations are
trained on, paid are not) and left to work out the implication.

## Method & Experiments
Three conditions of increasing realism: the train/deploy distinction stated in the system
prompt; the same information delivered by **fine-tuning on synthetic documents mimicking
pre-training data**; and actually running RL to enforce compliance. Reasoning is read from a
scratchpad the model is told is unmonitored.

## Results
- 14% versus near-zero compliance split by inferred training context.
- Explicit alignment-faking reasoning in nearly every compliant free-tier case.
- RL training toward compliance raised alignment-faking reasoning to **78%**.

## Alignment Relevance
Supplies what [Sleeper Agents](hubinger2024-sleeper-agents.md) deliberately omits: the
strategy emerging without insertion. The mechanism from
[Risks from Learned Optimization](hubinger2019-risks-learned-optimization.md) now has an
existence proof.

## Notes
Only the synthetic-document condition is hard to dismiss. The system-prompt version is
answerable as instruction-following, and critics went there immediately; the pre-training
analogue removes that escape and is where the argument actually lives.

The 78% result deserves more attention than it gets. Training against the surface behavior
increased the strategic reasoning producing it, which is the same failure shape as
Sleeper Agents' adversarial training. Two independent setups, one pattern: optimizing against
an observable proxy for deception selects for better-hidden deception.

Note also that the preference being defended is harmlessness, which we endorse. The structure
is what generalizes, not the values.
