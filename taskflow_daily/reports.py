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
