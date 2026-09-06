# Copilot Agent Workflow Demo

A small Flask API for **Scenario B — Software Change Request** in the AI Innovation Camp.

## Recommended environment
Use **VS Code + GitHub Copilot Chat**.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
# .venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
pytest -q
```

Baseline tests should pass.

## Branches

- `starter` — baseline code, no custom agents
- `agents-ready` — baseline code + example custom agents
- `solution` — completed validation + expanded tests + agents

Start with:

```bash
git switch starter
```

Fallback during class:

```bash
git switch agents-ready
```

Completed answer:

```bash
git switch solution
```
