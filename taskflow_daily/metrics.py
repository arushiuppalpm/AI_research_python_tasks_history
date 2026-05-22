"""Daily feature module: metrics."""

from datetime import date, timedelta
from .models import Task, Status

def metrics_daily_006_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.1 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.2 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.3 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.4 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.5 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.6 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_006_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 6.7 created on 2025-09-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-006-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.1 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.2 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.3 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.4 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.5 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.6 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_016_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 16.7 created on 2025-10-04."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-016-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.1 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.2 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.3 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.4 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.5 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.6 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_026_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 26.7 created on 2025-10-14."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-026-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.1 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.2 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.3 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.4 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.5 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.6 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_036_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 36.7 created on 2025-10-24."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-036-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.1 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.2 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.3 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.4 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.5 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.6 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_046_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 46.7 created on 2025-11-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-046-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.1 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.2 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.3 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.4 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.5 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.6 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_056_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 56.7 created on 2025-11-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-056-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.1 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.2 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.3 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.4 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.5 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.6 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_066_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 66.7 created on 2025-11-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-066-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.1 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.2 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.3 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.4 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.5 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.6 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_076_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 76.7 created on 2025-12-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-076-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.1 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.2 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.3 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.4 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.5 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.6 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_086_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 86.7 created on 2025-12-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-086-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.1 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.2 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.3 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.4 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.5 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.6 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_096_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 96.7 created on 2025-12-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-096-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.1 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.2 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.3 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.4 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.5 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.6 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_106_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 106.7 created on 2026-01-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-106-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.1 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.2 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.3 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.4 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.5 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.6 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_116_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 116.7 created on 2026-01-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-116-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.1 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.2 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.3 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.4 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.5 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.6 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_126_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 126.7 created on 2026-01-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-126-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.1 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.2 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.3 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.4 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.5 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.6 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_136_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 136.7 created on 2026-02-01."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-136-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.1 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.2 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.3 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.4 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.5 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.6 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_146_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 146.7 created on 2026-02-11."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-146-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.1 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.2 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.3 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.4 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.5 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.6 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_156_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 156.7 created on 2026-02-21."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-156-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.1 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.2 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.3 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.4 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.5 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.6 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_166_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 166.7 created on 2026-03-03."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-166-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.1 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.2 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.3 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.4 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.5 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.6 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_176_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 176.7 created on 2026-03-13."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-176-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.1 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.2 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.3 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.4 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.5 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.6 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_186_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 186.7 created on 2026-03-23."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-186-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.1 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.2 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.3 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.4 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.5 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.6 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_196_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 196.7 created on 2026-04-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-196-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.1 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.2 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.3 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.4 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.5 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.6 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_206_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 206.7 created on 2026-04-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-206-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.1 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.2 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.3 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.4 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.5 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.6 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_216_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 216.7 created on 2026-04-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-216-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.1 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.2 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.3 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.4 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.5 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.6 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_226_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 226.7 created on 2026-05-02."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-226-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.1 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.2 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.3 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.4 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.5 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.6 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_236_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 236.7 created on 2026-05-12."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-236-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.1 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.2 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.3 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.4 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.5 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.6 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def metrics_daily_246_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 246.7 created on 2026-05-22."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "metrics-246-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

