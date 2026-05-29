# Add calendar planning view

## Branch

`feature/calendar-planning-view`

## Summary

- Adds week planning helpers that group upcoming tasks by date.
- Adds focused code changes under `taskflow_daily/calendar.py`.
- Adds tests for the new behavior.

## Verification

- `python -m compileall taskflow_daily tests`
- `python -m pytest`

## Suggested Pull Request Body

This PR keeps the TaskFlow Daily codebase moving with a focused feature update. It adds a small, tested helper that can be reviewed independently from the daily history branch.
