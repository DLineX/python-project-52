from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse_lazy
from faker import Faker

from task_manager.statuses.models import Status
from task_manager.users.models import User


class TestStatuses(TestCase):
    def setUp(self):
        self.client = Client()
        self.faker_client = Faker()
        self.faker_username = self.faker_client.user_name()
        self.faker_password = self.faker_client.password(length=8)
        self.user_client = User.objects.create_user(
            username=self.faker_username, password=self.faker_password)
        self.user_client.save()
        self.name = self.faker_client.pystr()
        self.status = Status.objects.create(name=self.name,)
        self.status.save()

    def delete_status(self):
        self.user_client.delete()
        self.status.delete()

    def test_create(self):
        request = self.client.post(reverse_lazy('create_status'),
                                   {'name': 'testStatus'}, )
        self.assertEqual(request.status_code, HTTPStatus.FOUND)

    def test_update(self, status):
        request = self.client.post(reverse_lazy('update_status', status.id),
                                   {'name': 'testUpdate'}, )
        updated_status = Status.objects.get(name='testUpdate')
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        self.assertEqual(status.id, updated_status.id)

    def test_delete(self, status):
        request = self.client.post(reverse_lazy('delete_status', status.id),)
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        with self.assertRaises(status.DoesNotExist):
            Status.objects.get(pk=status.id)

    def test_status(self):
        self.client.force_login(self.user_client)
        request = self.client.get(reverse_lazy('statuses_list'))
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.test_create()
        self.test_update(self.status)
        self.test_delete(self.status)
