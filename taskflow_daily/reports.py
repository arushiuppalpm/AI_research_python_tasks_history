from .models import Task


def task_row(task: Task) -> dict[str, object]:
    return {
        "id": task.task_id,
        "title": task.title,
        "status": task.status.value,
        "priority": task.priority,
        "project": task.project,
        "tags": list(task.tags),
    }
def reports_daily_002_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.1 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.2 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.3 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.4 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.5 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.6 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_002_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 2.7 created on 2025-09-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-002-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.1 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.2 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.3 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.4 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.5 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.6 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_012_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 12.7 created on 2025-09-30."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-012-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.1 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.2 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.3 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.4 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.5 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.6 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_022_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 22.7 created on 2025-10-10."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-022-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_01(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.1 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-01",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_02(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.2 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-02",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_03(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.3 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-03",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_04(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.4 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-04",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_05(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.5 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-05",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_06(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.6 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-06",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

def reports_daily_032_07(tasks: list[Task], reference: date | None = None) -> dict[str, object]:
    """Daily taskflow feature 32.7 created on 2025-10-20."""
    today = reference or date.today()
    active = [task for task in tasks if task.status != Status.DONE]
    completed = [task for task in tasks if task.status == Status.DONE]
    blocked = [task for task in tasks if task.status == Status.BLOCKED]
    due_soon = [task for task in active if task.due is not None and task.due <= today + timedelta(days=7)]
    high_priority = [task for task in active if task.priority <= 2]
    projects = sorted({task.project for task in tasks})
    tags = sorted({tag for task in tasks for tag in task.tags})
    return {
        "feature": "reports-032-07",
        "total": len(tasks),
        "active": len(active),
        "completed": len(completed),
        "blocked": len(blocked),
        "due_soon": len(due_soon),
        "high_priority": len(high_priority),
        "projects": projects,
        "tags": tags,
        "reference": today.isoformat(),
    }

