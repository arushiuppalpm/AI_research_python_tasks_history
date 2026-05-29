from taskflow_daily.models import Task
from taskflow_daily.automation import pr_ready_feature_04


def test_pr_ready_feature_04_summarizes_tasks():
    task = Task(title="PR task", project="research")
    task.add_tag("demo")
    result = pr_ready_feature_04([task])
    assert result["active"] == 1
    assert result["projects"] == ["research"]
    assert result["tags"] == ["demo"]
