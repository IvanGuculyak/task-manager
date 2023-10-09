from django.test import TestCase

from tasks.forms import WorkerCreationForm
from tasks.models import Position


class FormsTests(TestCase):
    def test_worker_creation_form_with_position_first_last_name_is_valid(self):
        position = Position.objects.create(name="test_position")
        form_data = {
            "username": "new_user",
            "password1": "user_test1234",
            "password2": "user_test1234",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "position": position,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
