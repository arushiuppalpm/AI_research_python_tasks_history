from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Any
import uuid


class Status(str, Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    BLOCKED = "blocked"


@dataclass(slots=True)
class Task:
    title: str
    description: str = ""
    status: Status = Status.TODO
    priority: int = 3
    due: date | None = None
    tags: list[str] = field(default_factory=list)
    project: str = "inbox"
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict[str, Any] = field(default_factory=dict)

    def mark_done(self) -> None:
        self.status = Status.DONE
        self.updated_at = datetime.utcnow()

    def add_tag(self, tag: str) -> None:
        cleaned = tag.strip().lower()
        if cleaned and cleaned not in self.tags:
            self.tags.append(cleaned)
            self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority,
            "due": self.due.isoformat() if self.due else None,
            "tags": list(self.tags),
            "project": self.project,
            "task_id": self.task_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "metadata": dict(self.metadata),
        }
