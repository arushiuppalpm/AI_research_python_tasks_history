"""Daily feature module: validation."""

from datetime import date, timedelta
from .models import Task, Status

def validation_daily_009_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.1 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-01",
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

def validation_daily_009_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.2 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-02",
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

def validation_daily_009_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.3 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-03",
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

def validation_daily_009_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.4 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-04",
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

def validation_daily_009_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.5 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-05",
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

def validation_daily_009_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.6 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-06",
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

def validation_daily_009_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 9.7 created on 2025-09-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-009-07",
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

def validation_daily_019_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.1 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-01",
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

def validation_daily_019_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.2 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-02",
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

def validation_daily_019_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.3 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-03",
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

def validation_daily_019_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.4 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-04",
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

def validation_daily_019_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.5 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-05",
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

def validation_daily_019_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.6 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-06",
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

def validation_daily_019_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 19.7 created on 2025-10-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-019-07",
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

def validation_daily_029_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.1 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-01",
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

def validation_daily_029_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.2 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-02",
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

def validation_daily_029_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.3 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-03",
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

def validation_daily_029_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.4 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-04",
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

def validation_daily_029_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.5 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-05",
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

def validation_daily_029_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.6 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-06",
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

def validation_daily_029_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 29.7 created on 2025-10-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-029-07",
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

def validation_daily_039_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.1 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-01",
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

def validation_daily_039_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.2 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-02",
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

def validation_daily_039_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.3 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-03",
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

def validation_daily_039_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.4 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-04",
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

def validation_daily_039_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.5 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-05",
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

def validation_daily_039_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.6 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-06",
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

def validation_daily_039_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 39.7 created on 2025-10-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-039-07",
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

def validation_daily_049_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.1 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-01",
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

def validation_daily_049_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.2 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-02",
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

def validation_daily_049_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.3 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-03",
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

def validation_daily_049_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.4 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-04",
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

def validation_daily_049_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.5 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-05",
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

def validation_daily_049_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.6 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-06",
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

def validation_daily_049_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 49.7 created on 2025-11-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-049-07",
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

def validation_daily_059_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.1 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-01",
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

def validation_daily_059_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.2 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-02",
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

def validation_daily_059_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.3 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-03",
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

def validation_daily_059_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.4 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-04",
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

def validation_daily_059_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.5 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-05",
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

def validation_daily_059_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.6 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-06",
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

def validation_daily_059_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 59.7 created on 2025-11-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-059-07",
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

def validation_daily_069_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.1 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-01",
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

def validation_daily_069_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.2 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-02",
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

def validation_daily_069_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.3 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-03",
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

def validation_daily_069_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.4 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-04",
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

def validation_daily_069_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.5 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-05",
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

def validation_daily_069_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.6 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-06",
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

def validation_daily_069_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 69.7 created on 2025-11-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-069-07",
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

def validation_daily_079_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.1 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-01",
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

def validation_daily_079_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.2 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-02",
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

def validation_daily_079_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.3 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-03",
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

def validation_daily_079_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.4 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-04",
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

def validation_daily_079_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.5 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-05",
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

def validation_daily_079_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.6 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-06",
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

def validation_daily_079_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 79.7 created on 2025-12-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-079-07",
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

def validation_daily_089_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.1 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-01",
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

def validation_daily_089_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.2 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-02",
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

def validation_daily_089_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.3 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-03",
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

def validation_daily_089_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.4 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-04",
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

def validation_daily_089_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.5 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-05",
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

def validation_daily_089_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.6 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-06",
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

def validation_daily_089_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 89.7 created on 2025-12-16."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-089-07",
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

def validation_daily_099_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.1 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-01",
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

def validation_daily_099_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.2 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-02",
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

def validation_daily_099_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.3 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-03",
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

def validation_daily_099_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.4 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-04",
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

def validation_daily_099_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.5 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-05",
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

def validation_daily_099_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.6 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-06",
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

def validation_daily_099_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 99.7 created on 2025-12-26."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-099-07",
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

def validation_daily_109_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.1 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-01",
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

def validation_daily_109_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.2 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-02",
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

def validation_daily_109_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.3 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-03",
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

def validation_daily_109_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.4 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-04",
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

def validation_daily_109_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.5 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-05",
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

def validation_daily_109_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.6 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-06",
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

def validation_daily_109_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 109.7 created on 2026-01-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-109-07",
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

def validation_daily_119_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.1 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-01",
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

def validation_daily_119_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.2 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-02",
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

def validation_daily_119_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.3 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-03",
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

def validation_daily_119_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.4 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-04",
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

def validation_daily_119_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.5 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-05",
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

def validation_daily_119_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.6 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-06",
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

def validation_daily_119_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 119.7 created on 2026-01-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-119-07",
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

def validation_daily_129_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.1 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-01",
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

def validation_daily_129_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.2 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-02",
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

def validation_daily_129_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.3 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-03",
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

def validation_daily_129_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.4 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-04",
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

def validation_daily_129_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.5 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-05",
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

def validation_daily_129_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.6 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-06",
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

def validation_daily_129_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 129.7 created on 2026-01-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "validation-129-07",
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

