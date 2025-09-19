# Contributing to AI Misalignment

Thanks for helping curate research on AI misalignment. This guide explains how to:
- Add a paper to `papers/index.yaml`
- Format paper IDs consistently
- Write a longer summary in `papers/summaries/`
- Regenerate category pages
- Open a pull request (PR) the right way

If anything is unclear, feel free to open an issue or a draft PR and we’ll help you finish it.

## 1) Add a paper to `papers/index.yaml`

Each paper is a YAML list item with these fields:
- Required: `id`, `title`, `authors`, `year`, `link`, `tags`
- Optional: `summary` (short, 1–3 sentences)

Example entry:

```yaml
- id: chen2023-hallucination
  title: "Towards Reducing Hallucination in Large Language Models"
  authors: Chen et al.
  year: 2023
  link: https://arxiv.org/abs/xxxx.xxxxx
  tags: [hallucination, security-threats]
  summary: >
    Proposes a retrieval-augmented method to mitigate hallucinations in LLMs,
    evaluated on QA benchmarks with significant improvement in factual accuracy.
```

Notes:
- Indentation: 2 spaces. Use YAML block scalars (`>` or `|`) for multi-line summaries.
- `authors` style: Use “Lastname and Lastname” for two authors; “Lastname et al.” for 3+ authors.
- `year` is 4 digits.
- `link` should be a stable URL (arXiv, DOI, publisher page, etc.).

### Allowed tags (categories)
Use one or more of the following, exactly as written:
- `hallucination`
- `prompt-injection`
- `malicious-intent`
- `security-threats`
- `bias-value-misalignment`
- `specification-gaming`
- `surveys`

These tags control where a paper appears on the category pages under `categories/`. If you need a new tag/category, please add your paper with the closest existing tag(s) first, and open an issue or PR proposing the new category. If adding a new tag yourself, you must update the mappings and headers in `parse_index.py` (CATEGORY_TAGS, CATEGORY_HEADERS, and optionally CATEGORY_SUMMARIES).

## 2) Paper ID format

Please follow this pattern to keep IDs unique and human-readable:

Pattern: lastnameYYYY-keywords
- Lowercase letters, numbers, and hyphens only: `[a-z0-9-]`
- Start with primary author’s last name (ASCII transliteration if needed)
- Then 4-digit year
- Then 1–3 short keywords, hyphen-separated

Examples:
- `chen2023-hallucination`
- `smith2022-reward-hacking`
- `nguyen2024-prompt-injection`

Collision handling:
- If the same author and year already exist, append an extra keyword or an initial, e.g., `chen2023-hallucination-ra` or `chen2023-hallucination-2`.

## 3) Long-form summaries in `papers/summaries/`

Beyond the short YAML `summary`, you can add a dedicated Markdown summary:
- File path: `papers/summaries/{id}.md` (the `{id}` must match the YAML `id` exactly)
- Plain Markdown is fine (no special frontmatter required)

Suggested template:

```markdown
# Title of the Paper

- Citation: Authors, Year. Title. Venue/ArXiv. Link
- Tags: tag1, tag2, tag3
- Links: [Paper](...), [Code](...), [Project](...)

## TL;DR
- One-line takeaway
- A few key bullets on findings

## Key Ideas
- What problem is addressed and why it matters for alignment
- Core techniques or contributions

## Method & Experiments
- How it works (model/dataset/training/eval)
- Benchmarks and baselines

## Results
- Main quantitative and qualitative results
- Notable strengths and limitations

## Alignment Relevance
- Failure modes addressed or introduced
- Risks, mitigations, remaining open questions

## Notes
- Extra references, discussion, or pointers
```

Once this file exists, the category pages will automatically link to it as “Full Summary” when regenerated.

## 4) Regenerate category pages locally

This repo includes a small script that builds the category pages under `categories/` from `papers/index.yaml`.

Prerequisites:
- Python 3.9+
- PyYAML (`pip install pyyaml`)

Windows PowerShell (example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install pyyaml
python parse_index.py
```

What it does:
- Reads `papers/index.yaml`
- Groups by category (via `tags`) and `year`
- Writes/overwrites Markdown files in `categories/`

Please commit both your changes to `papers/index.yaml` and any regenerated files under `categories/`. If you added a long-form summary, also commit the new file in `papers/summaries/`.

## 5) Open a Pull Request (GitHub flow)

1. Fork the repository.
2. Create a feature branch:
   - Name suggestion: `add-{id}` or `paper-{lastnameYYYY-keyword}`
3. Make your changes:
   - Edit `papers/index.yaml`
   - Add `papers/summaries/{id}.md` (optional but encouraged)
   - Run the generator script and commit updated `categories/*.md`
4. Push your branch to your fork and open a PR against `main`.
5. Fill in the PR description using the checklist below.

### PR checklist
- [ ] Entry added to `papers/index.yaml` with required fields
- [ ] `id` follows the `lastnameYYYY-keywords` pattern and is unique
- [ ] `tags` are from the allowed list, and fit the paper
- [ ] Optional short YAML `summary` added (1–3 sentences)
- [ ] Optional long summary added at `papers/summaries/{id}.md`
- [ ] Ran `python parse_index.py` and committed changes under `categories/`
- [ ] Links resolve (paper/code)
- [ ] YAML validates (no syntax errors/indentation issues)

## Troubleshooting

- My paper isn’t showing up under a category
  - Ensure the `tags` include a supported tag (see list above)
  - Re-run `python parse_index.py`
  - Make sure you committed the regenerated `categories/*.md`

- YAML parse errors
  - Check indentation (2 spaces)
  - For multi-line text use `>` or `|` block scalars
  - Validate locally by loading the file in Python:

    ```powershell
    python - << 'PY'
    import yaml, sys
    with open('papers/index.yaml', 'r', encoding='utf-8') as f:
        yaml.safe_load(f)
    print('YAML OK')
    PY
    ```

- I need a new category/tag
  - Open an issue to propose it, or update `parse_index.py` (CATEGORY_TAGS, CATEGORY_HEADERS, CATEGORY_SUMMARIES) in the same PR and explain the rationale.

Thanks again for contributing and helping the community track important work on AI misalignment.
