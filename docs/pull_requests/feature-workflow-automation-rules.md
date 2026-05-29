# Add workflow automation rules

## Branch

`feature/workflow-automation-rules`

## Summary

- Adds rule helpers for moving blocked, active, and completed tasks through a simple workflow.
- Adds focused code changes under `taskflow_daily/automation.py`.
- Adds tests for the new behavior.

## Verification

- `python -m compileall taskflow_daily tests`
- `python -m pytest`

## Suggested Pull Request Body

This PR keeps the TaskFlow Daily codebase moving with a focused feature update. It adds a small, tested helper that can be reviewed independently from the daily history branch.
