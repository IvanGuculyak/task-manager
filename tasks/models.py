from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return (
            f"{self.username} "
            f"Full name: {self.first_name} {self.last_name} "
            f"Position: {self.position}"
        )

    def get_absolute_url(self):
        return reverse(
            "tasks:worker-detail",
            args=[str(self.id)]
        )


class Task(models.Model):
    PRIORITY = [
        ("Urgent", "Urgent"),
        ("Height", "Height"),
        ("Medium", "Medium"),
        ("Low", "Low")
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=64,
        choices=PRIORITY,
        default="Medium"
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

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} priority: {self.priority}"

    def get_absolute_url(self):
        return reverse(
            "tasks:task-detail",
            args=[str(self.id)]
        )
