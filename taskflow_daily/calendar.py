"""Daily feature module: calendar."""

from datetime import date, timedelta
from .models import Task, Status

def calendar_daily_007_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.1 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.2 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.3 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.4 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.5 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.6 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_007_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 7.7 created on 2025-09-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-007-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.1 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.2 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.3 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.4 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.5 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.6 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_017_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 17.7 created on 2025-10-05."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-017-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.1 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.2 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.3 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.4 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.5 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.6 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_027_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 27.7 created on 2025-10-15."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-027-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.1 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.2 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.3 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.4 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.5 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.6 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def calendar_daily_037_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 37.7 created on 2025-10-25."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "calendar-037-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

