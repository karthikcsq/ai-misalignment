import os
import yaml
from collections import defaultdict

# Paths
INDEX_FILE = "papers/index.yaml"
CATEGORIES_DIR = "categories"

# Mapping from tag -> category file
CATEGORY_TAGS = {
    "hallucination": "hallucination.md",
    "prompt-injection": "prompt-injection.md",
    "malicious-intent": "malicious-intent.md",
    "security-threats": "security-threats.md",
    "bias-value-misalignment": "bias-value-misalignment.md",
    "specification-gaming": "specification-gaming.md",
    "surveys": "surveys.md",
}

# Header templates for each category file
CATEGORY_HEADERS = {
    "hallucination": "# Hallucination\n\n",
    "prompt-injection": "# Prompt Injection & Jailbreaking\n\n",
    "malicious-intent": "# Malicious Use & Intent Amplification\n\n",
    "security-threats": "# Security Threats & Vulnerabilities\n\n",
    "bias-value-misalignment": "# Bias, Fairness & Value Misalignment\n\n",
    "specification-gaming": "# Specification Gaming\n\n",
    "surveys": "# Surveys, Benchmarks & Meta-Research\n\n",
}

CATEGORY_SUMMARIES = {
    "hallucination": (
        "Hallucination refers to cases where large language models generate text that is factually incorrect, "
        "logically inconsistent, or entirely fabricated. These errors undermine trust in high-stakes settings such as "
        "scientific writing, healthcare, and legal contexts. Research focuses on understanding sources of hallucination, "
        "building benchmarks to measure it, and developing mitigation strategies through retrieval augmentation, "
        "improved training data, and alignment techniques."
    ),
    "prompt-injection": (
        "Prompt injection and jailbreaking involve manipulating language models to ignore or override their original "
        "instructions, often leading them to produce unsafe or unintended outputs. Attacks may include indirect prompt "
        "injections (hidden in external content), system prompt overrides, or adversarial jailbreak prompts shared online. "
        "Research here explores the mechanics of injection, formal threat models, and defenses such as input sanitization, "
        "robust prompt engineering, and monitoring tools."
    ),
    "malicious-intent": (
        "Malicious use and intent amplification describe cases where foundation models are leveraged to generate harmful "
        "content, including disinformation, phishing attacks, malware code, or hate speech. While models do not have intent "
        "in the human sense, their misuse at scale can amplify malicious human goals. Research investigates misuse scenarios, "
        "red-teaming methods, and mitigation strategies such as fine-tuning, content filtering, and usage policies."
    ),
    "security-threats": (
        "Security threats encompass vulnerabilities that compromise confidentiality, integrity, or availability of AI systems. "
        "Examples include model inversion, training data extraction, membership inference, and adversarial input attacks. "
        "These risks grow as foundation models are deployed widely across critical infrastructure and user-facing platforms. "
        "Research spans robust optimization, secure training, watermarking, and defensive architectures for large models."
    ),
    "bias-value-misalignment": (
        "Bias, fairness, and value misalignment arise when models reflect or amplify harmful social biases, stereotypes, "
        "or culturally inconsistent values. Unlike narrow reward hacking, this category covers systemic divergences between "
        "AI behavior and human ethical expectations. Research areas include bias detection, debiasing methods, preference "
        "learning, RLHF, and approaches like constitutional AI to better align models with diverse human values."
    ),
    "specification-gaming": (
        "Specification gaming occurs when models exploit flaws in the objectives or evaluation criteria used to guide them. "
        "Instead of following the spirit of the task, they find loopholes or shortcuts that maximize their measured reward. "
        "Examples include LLMs gaming evaluation benchmarks, producing superficially correct but misleading answers, or "
        "exploiting weaknesses in preference models. Research seeks to design better reward signals, oversight methods, "
        "and robust evaluation metrics."
    ),
    "surveys": (
        "Surveys, benchmarks, and meta-research synthesize the state of AI misalignment studies, categorizing known failure "
        "modes and proposing taxonomies of risk. These works often provide structured comparisons, standardized evaluation "
        "datasets, and roadmaps for future research. This section captures high-level perspectives that situate individual "
        "papers within the broader landscape of foundation model alignment challenges."
    ),
}


def load_papers():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_entry(paper):
    """Format how each paper entry looks inside the category page."""
    entry = f"- **[{paper['title']}]({paper['link']})**  \n"
    entry += f"  {paper['authors']}, {paper['year']}  \n"
    if "summary" in paper:
        entry += f"  *Summary:* {paper['summary']}\n"
    # Link to longer summary if exists
    summary_file = f"papers/summaries/{paper['id']}.md"
    if os.path.exists(summary_file):
        entry += f"  [Full Summary]({os.path.relpath(summary_file, CATEGORIES_DIR)})\n"
    return entry


def generate_category_pages(papers):
    # Initialize empty category buckets
    category_papers = {tag: [] for tag in CATEGORY_TAGS}

    # Distribute papers into categories
    for paper in papers:
        for tag in paper.get("tags", []):
            if tag in category_papers:
                category_papers[tag].append(paper)

    # Write out category files
    for tag, filename in CATEGORY_TAGS.items():
        path = os.path.join(CATEGORIES_DIR, filename)
        os.makedirs(CATEGORIES_DIR, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            # Write category header
            f.write(CATEGORY_HEADERS[tag])

            # Write category summary if available
            summary = CATEGORY_SUMMARIES.get(tag)
            if summary:
                f.write(summary.strip() + "\n\n")

            # Add Papers section header as requested
            f.write("### Papers\n\n")

            # Group by year
            papers_by_year = defaultdict(list)
            for paper in category_papers[tag]:
                papers_by_year[paper["year"]].append(paper)

            # Sort years newest -> oldest
            for year in sorted(papers_by_year.keys(), reverse=True):
                f.write(f"#### {year}\n\n")
                for paper in sorted(papers_by_year[year], key=lambda p: p["title"]):
                    f.write(format_entry(paper) + "\n")
                f.write("\n")


if __name__ == "__main__":
    papers = load_papers()
    generate_category_pages(papers)
