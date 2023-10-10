from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Position


class AdminSiteTests(TestCase):
    def setUp(self):
        position = Position.objects.create(
            name="developer"
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test1234"
        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="worker1234",
            position=position
        )

    def test_worker_position_listed(self):
        url = reverse("admin:tasks_worker_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:tasks_worker_change", args=[self.worker.id])
        response = self.client.get(url)
        self.assertContains(response, self.worker.position)
