from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True
    )

    def __str__(self):
        return f"{self.username} " \
               f"Full name: {self.first_name} {self.last_name} " \
               f"Position: {self.position}"


class Task(models.Model):
    PRIORITY = [
        ("UR", "Urgent"),
        ("HG", "Height"),
        ("MD", "Medium"),
        ("LW", "Low")
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY,
        default="MD"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    def __str__(self):
        return f"{self.name} priority: {self.priority}"

