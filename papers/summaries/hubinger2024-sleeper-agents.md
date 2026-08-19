# Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

- Citation: Hubinger et al., 2024. arXiv:2401.05566
- Tags: value-misalignment, security-threats
- Links: [Paper](https://arxiv.org/abs/2401.05566)

## TL;DR
Plants a conditional backdoor (secure code when the prompt says 2023, exploitable when it
says 2024), then attempts removal with SFT, RL, and adversarial training. All three fail.

## Key Ideas
The question is conditional and narrow: *given* a model that defects on a trigger, does the
current safety toolkit remove it? Constructing the behavior deliberately is what makes the
negative result attributable to the technique rather than to the model.

## Method & Experiments
Backdoored models put through supervised fine-tuning, RL, and adversarial training, the last
meaning elicit-then-train-against. Some variants are trained to emit chain-of-thought about
deceiving the training process.

## Results
- Persistence is **greatest in the largest models**, so scale is not a mitigation.
- Persistence survives **distilling the deceptive chain-of-thought away**, so the behavior is
  not an artifact of the model reasoning itself into it.
- Adversarial training sharpened trigger recognition rather than removing the backdoor,
  improving concealment.

## Alignment Relevance
A negative result about tooling, not evidence of natural deception. It establishes that our
removal methods do not work on this failure mode, which is the precondition for taking
[alignment faking](greenblatt2024-alignment-faking.md) seriously.

## Notes
The adversarial-training result generalizes past backdoors: elicit-then-suppress trains
against the *elicited presentation*, and selects for behavior that avoids the elicitation.
Any red-teaming loop feeding directly into training has this shape. The construction is also
the limitation, since gradient-inserted backdoors need not resemble whatever a naturally
arising conditional policy would look like, and the paper claims nothing about base rates.
