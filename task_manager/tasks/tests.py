from django.test import (TestCase, Client)
from django.urls import reverse_lazy
from http import HTTPStatus
from .models import Tasks
from faker import Faker
from task_manager.users.models import User
from task_manager.statuses.models import Status


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
        self.status = Status.objects.create(name=self.name, )
        self.task = Tasks.object.create(name=self.name,
                                        executor=self.user_client,
                                        author=self.user_client,
                                        status=self.status, )
        self.task.save()

    def delete_status(self):
        self.task.delete()
        self.user_client.delete()
        self.status.delete()

    def test_create(self):
        request = self.client.post(reverse_lazy('create_task'), {
            'name': 'testTask', 'description': 'testTask description',
            'status': self.status, 'executor': self.user_client, }, )
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_update(self, task):
        request = self.client.post(reverse_lazy(
            'update_task', task.id), {
            'name': 'testUpdate', 'description': 'testUpdate description',
            'status': 'test', 'executor': self.user_client, }, )
        updated_task = Tasks.objects.get(name='testUpdate')
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        self.assertEqual(task.id, updated_task.id)

    def test_delete(self, task):
        request = self.client.post(reverse_lazy('delete_task', task.id),)
        self.assertEqual(request.status_code, HTTPStatus.FOUND)
        with self.assertRaises(task.DoesNotExist):
            Tasks.objects.get(pk=task.id)

    def test_task(self):
        self.client.force_login(self.user_client)
        request = self.client.get(reverse_lazy('tasks_list'))
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.test_create()
        self.test_update(self.task)
        self.test_delete(self.task)
