from django.contrib.auth import get_user_model
from django.test import TestCase

from tasks.models import Position, TaskType, Task


class ModelTest(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="test_position"
        )
        self.assertEqual(str(position), "test_position")

    def test_task_type_str(self):
        task_type = TaskType.objects.create(
            name="New feature"
        )
        self.assertEqual(str(task_type), "New feature")

    def test_task_str(self):
        task_type = TaskType.objects.create(
            name="New feature"
        )
        task = Task.objects.create(
            name="Add test",
            deadline="2023-11-11",
            task_type=task_type
        )
        self.assertEqual(
            str(task),
            f"{task.name} priority: {task.priority} type: {task.task_type}"
        )

    def test_worker_str(self):
        position = Position.objects.create(
            name="test_position"
        )
        worker = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
            position=position
        )
        self.assertEqual(
            str(worker),
            f"{worker.username} "
            f"Full name: {worker.first_name} {worker.last_name} "
            f"Position: {worker.position}"
        )
        self.assertTrue(worker.check_password("test1234"))