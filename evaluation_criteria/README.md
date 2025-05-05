# Evaluation Criteria for AI Code Review

This folder contains markdown files that define the criteria used by the AI model (e.g., Claude) to review pull request diffs.

Each `.md` file focuses on a specific category like code quality, readability, bugs, optimization, etc.

## How to Add a New Criterion

1. Create a new `.md` file in this folder.
2. Use a clear and descriptive filename (e.g., `scalability.md`).
3. Use the following structure:

```markdown
## <Criterion Title>

Brief description of what this criterion evaluates.

### Consider:
- Point 1
- Point 2
- Point 3
