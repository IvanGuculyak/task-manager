from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from tasks.models import Position, TaskType, Task, Worker


def index(request: HttpRequest) -> HttpResponse:
    num_position = Position.objects.count()
    num_task_type = TaskType.objects.count()
    num_task = Task.objects.count()
    num_worker = Worker.objects.count()

    context = {
        "num_position": num_position,
        "num_task_type": num_task_type,
        "num_task": num_task,
        "num_worker": num_worker
    }

    return render(
        request,
        "tasks/index.html",
        context
    )


class PositionListView(generic.ListView):
    model = Position


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "tasks/task_type_list.html"
    context_object_name = "task_type_list"


class TaskListView(generic.ListView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker
