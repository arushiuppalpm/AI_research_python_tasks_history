from taskflow_daily.models import Task
from taskflow_daily.core import active_tasks


def test_task_can_be_completed():
    task = Task(title="Write daily code")
    assert active_tasks([task]) == [task]
    task.mark_done()
    assert active_tasks([task]) == []
def test_daily_generated_case_001():
    task = Task(title="Daily generated task 1", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_008():
    task = Task(title="Daily generated task 8", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_015():
    task = Task(title="Daily generated task 15", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

