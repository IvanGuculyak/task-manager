from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Position, Worker

POSITION_URL = reverse("tasks:position-list")


class PublicPositionTest(TestCase):
    def test_login_required(self):
        response = self.client.get(POSITION_URL)
        self.assertNotEquals(response.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="developer"),
        Position.objects.create(name="team_leader")
        response = self.client.get(POSITION_URL)
        self.assertEqual(response.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(
            response,
            "tasks/position_list.html"
        )


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password1234"
        )
        self.client.force_login(self.user)

    def test_create_worker(self):
        position = Position.objects.create(name="test_position")
        form_data = {
            "username": "new_user",
            "password1": "user_test1234",
            "password2": "user_test1234",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "position": position.id,
        }

        self.client.post(reverse("tasks:worker-create"), data=form_data)
        new_user = Worker.objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position.id, form_data["position"])
