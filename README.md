# 🤖 AI-Powered Code Review Automation with Anthropic Claude

> Automate intelligent, consistent, and scalable code reviews directly in your GitHub pull requests using Anthropic's Claude API.

## 📌 Overview

This repository implements a modular, CI-integrated code review framework that leverages Anthropic Claude to automatically review pull requests. The system analyzes code diffs, applies human-centric evaluation criteria, and posts structured, actionable feedback as PR comments.

## 🧠 Core Objectives

- **Automate** high-quality PR reviews at scale
- **Ensure consistency** using criteria-driven analysis
- **Enhance developer productivity** by reducing review latency
- **Utilize LLMs** to identify bugs, suggest improvements, and uphold coding standards

## 🛠️ System Architecture

```
GitHub PR Event ─┬─▶ GitHub Actions Workflow
                 │
                 └─▶ Python App (scripts/)
                      ├─ Fetch PR diff
                      ├─ Load evaluation criteria
                      ├─ Call Anthropic Claude API
                      ├─ Parse response
                      └─ Post PR comment via GitHub API
```

## 📁 Repository Structure

```
MLOps/
├── scripts/                   # Core logic
│   ├── main.py                # Entry point
│   ├── reviewer.py            # PR review pipeline
│   ├── github_utils.py        # GitHub API interaction
│   ├── anthropic_utils.py     # Claude API wrapper
│   ├── prompts.py             # Advanced prompt engineering templates
│   ├── config.py              # Environment and constants
│   └── utils.py               # Helpers (e.g., markdown criteria loader)
│
├── evaluation_criteria/       # Human-aligned review principles
│   ├── README.md              # Instructions for writing criteria
│   ├── code_quality.md
│   ├── performance.md
│   ├── documentation.md
│   └── security.md
│
├── .github/
│   └── workflows/
│       └── review.yml         # GitHub Actions CI pipeline
│
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### ✅ Prerequisites

- Python 3.10+
- GitHub Personal Access Token
- Anthropic Claude API Key

### 📥 Installation

```bash
git clone https://github.com/SYED-M-HUSSAIN/MLOps.git
cd MLOps
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```


### ▶️ Run Locally

```bash
python scripts/main.py
```

## 📜 Writing Evaluation Criteria

Evaluation files are structured markdown documents under `evaluation_criteria/`, allowing modularity, explainability, and transparency of the review system.

Each file should include sections such as:

```markdown
# Code Quality

### Positive Examples
- Uses meaningful variable names
- Follows single-responsibility principle

### Negative Examples
- Deeply nested conditionals
- Repetitive logic without abstraction
```

These files are parsed and embedded in the system prompt to guide Claude's analysis.

Refer to [`evaluation_criteria/README.md`](evaluation_criteria/README.md) for detailed authoring guidelines.

## 🤖 Prompt Engineering

Prompt templates are constructed in `scripts/prompts.py` using structured prompt engineering best practices:

- **System prompt** defines the reviewer's role and tone.
- **User prompt** includes code diffs and target instructions.
- Prompts are **contextualized** using evaluation criteria.

This separation enables maintainable and testable interactions with the LLM.

## 🔁 GitHub Actions Integration

The `.github/workflows/review.yml` pipeline triggers the review on PR open or update.

```yaml
on:
  pull_request:
    types: [opened, synchronize]
```

You can extend this pipeline to:
- Run tests on the Claude response
- Notify developers via Slack
- Auto-approve or label PRs

## 🧪 Testing and Validation

**Unit tests** (coming soon) will cover:

- Diff parsing logic
- Prompt formatting
- Claude response validation
- Markdown criteria loading

To run tests:

```bash
pytest tests/
```

## 🔐 Security Considerations

- **Secrets** such as API keys must be stored in GitHub Secrets or `.env` files.
- **LLM responses** are sandboxed and validated before GitHub posting.
- Avoid logging sensitive data.

## 🔄 Extending the System

You can easily:

- Add more criteria categories
- Support multi-file diffs
- Swap Claude with OpenAI/Gemini via modular prompt layers
- Track response accuracy with custom feedback loops

## 👥 Contributing

We welcome contributions in the form of:

- Improved prompts or criteria
- Support for additional models
- Enhancements to GitHub workflows
- Documentation improvements

Please follow [Semantic Commit Messages](https://www.conventionalcommits.org/) and open a PR with a detailed description.

## 📃 License

This project is released under the MIT License. See `LICENSE` for more information.

## 🔗 Resources

- [Anthropic Claude API Docs](https://docs.anthropic.com/)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Best Practices for LLM Apps](https://github.com/openai/openai-cookbook)