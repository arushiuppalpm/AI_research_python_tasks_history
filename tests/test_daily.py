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

def test_daily_generated_case_022():
    task = Task(title="Daily generated task 22", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_029():
    task = Task(title="Daily generated task 29", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_036():
    task = Task(title="Daily generated task 36", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_043():
    task = Task(title="Daily generated task 43", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_050():
    task = Task(title="Daily generated task 50", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_057():
    task = Task(title="Daily generated task 57", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_064():
    task = Task(title="Daily generated task 64", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_071():
    task = Task(title="Daily generated task 71", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_078():
    task = Task(title="Daily generated task 78", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_085():
    task = Task(title="Daily generated task 85", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_092():
    task = Task(title="Daily generated task 92", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_099():
    task = Task(title="Daily generated task 99", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_106():
    task = Task(title="Daily generated task 106", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_113():
    task = Task(title="Daily generated task 113", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_120():
    task = Task(title="Daily generated task 120", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_127():
    task = Task(title="Daily generated task 127", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_134():
    task = Task(title="Daily generated task 134", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_141():
    task = Task(title="Daily generated task 141", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_148():
    task = Task(title="Daily generated task 148", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_155():
    task = Task(title="Daily generated task 155", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_162():
    task = Task(title="Daily generated task 162", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_169():
    task = Task(title="Daily generated task 169", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_176():
    task = Task(title="Daily generated task 176", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

def test_daily_generated_case_183():
    task = Task(title="Daily generated task 183", priority=2, project="research")
    task.add_tag("daily")
    assert task.priority == 2
    assert "daily" in task.tags

