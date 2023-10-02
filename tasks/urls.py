from django.urls import path

from tasks.views import (
    index,
    TaskTypeListView,
    PositionListView, WorkerListView, TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list"
    )
]

app_name = "tasks"
