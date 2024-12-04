from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse_lazy
from faker import Faker

from task_manager.users.models import User

from .models import Labels


class TestTasks(TestCase):
    def setUp(self):
        self.client = Client()
        self.faker_client = Faker()
        self.faker_username = self.faker_client.user_name()
        self.faker_password = self.faker_client.password(length=8)
        self.user_client = User.objects.create_user(
            username=self.faker_username, password=self.faker_password)
        self.user_client.save()
        self.name = self.faker_client.pystr()
        self.labels = Labels.objects.create(name=self.name,)
        self.labels.save()

    def delete_label(self):
        self.user_client.delete()
        self.labels.delete()

    def test_create(self):
        request = self.client.post(reverse_lazy('create_label'),
                                   {'name': 'testLabel'}, )
        self.assertEqual(request.status_code, HTTPStatus.FOUND)

    def test_update(self, labels):
        request = self.client.post(reverse_lazy(
            'update_label', labels.id), {
            'name': 'testUpdate'}, )
        updated_labels = Labels.objects.get(name='testUpdate')
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        self.assertEqual(labels.id, updated_labels.id)

    def test_delete(self, labels):
        request = self.client.post(reverse_lazy('delete_label', labels.id),)
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        with self.assertRaises(labels.DoesNotExist):
            Labels.objects.get(pk=labels.id)

    def test_task(self):
        self.client.force_login(self.user_client)
        request = self.client.get(reverse_lazy('labels_list'))
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.test_create()
        self.test_update(self.labels)
        self.test_delete(self.labels)
