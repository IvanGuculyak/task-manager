from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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