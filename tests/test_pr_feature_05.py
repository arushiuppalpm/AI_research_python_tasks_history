from taskflow_daily.models import Task
from taskflow_daily.calendar import pr_ready_feature_05


def test_pr_ready_feature_05_summarizes_tasks():
    task = Task(title="PR task", project="research")
    task.add_tag("demo")
    result = pr_ready_feature_05([task])
    assert result["active"] == 1
    assert result["projects"] == ["research"]
    assert result["tags"] == ["demo"]
