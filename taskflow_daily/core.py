from datetime import date, timedelta
from statistics import mean
from .models import Task, Status


def active_tasks(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if task.status != Status.DONE]


def completed_tasks(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if task.status == Status.DONE]


def overdue_tasks(tasks: list[Task], today: date | None = None) -> list[Task]:
    current = today or date.today()
    return [task for task in active_tasks(tasks) if task.due is not None and task.due < current]
def core_daily_001_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.1 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.2 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.3 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.4 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.5 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.6 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_001_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 1.7 created on 2025-09-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-001-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.1 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.2 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.3 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.4 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.5 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.6 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_011_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 11.7 created on 2025-09-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-011-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.1 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.2 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.3 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.4 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.5 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.6 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_021_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 21.7 created on 2025-10-09."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-021-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.1 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.2 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.3 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.4 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.5 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.6 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_031_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 31.7 created on 2025-10-19."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-031-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.1 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.2 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.3 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.4 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.5 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.6 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_041_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 41.7 created on 2025-10-29."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-041-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.1 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.2 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.3 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.4 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.5 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.6 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_051_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 51.7 created on 2025-11-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-051-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.1 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.2 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.3 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.4 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.5 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.6 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_061_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 61.7 created on 2025-11-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-061-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.1 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.2 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.3 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.4 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.5 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.6 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_071_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 71.7 created on 2025-11-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-071-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.1 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.2 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.3 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.4 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.5 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.6 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_081_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 81.7 created on 2025-12-08."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-081-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.1 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.2 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.3 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.4 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.5 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.6 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_091_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 91.7 created on 2025-12-18."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-091-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.1 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.2 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.3 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.4 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.5 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.6 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_101_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 101.7 created on 2025-12-28."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-101-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.1 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.2 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.3 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.4 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.5 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.6 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_111_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 111.7 created on 2026-01-07."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-111-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.1 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.2 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.3 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.4 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.5 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.6 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_121_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 121.7 created on 2026-01-17."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-121-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.1 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.2 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.3 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.4 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.5 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.6 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_131_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 131.7 created on 2026-01-27."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-131-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.1 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.2 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.3 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.4 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.5 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.6 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def core_daily_141_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 141.7 created on 2026-02-06."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "core-141-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

