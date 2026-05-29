# Contributing

TaskFlow Daily uses small feature branches and focused pull requests.

## Workflow

1. Create a feature branch from `main`.
2. Keep code changes focused on one feature area.
3. Add or update tests when behavior changes.
4. Open a pull request with a short summary and verification notes.

## Local Checks

```bash
python -m compileall taskflow_daily tests
python -m pytest
```

## Pull Request Notes

Each pull request should include:

- What changed
- Why it changed
- How it was checked
