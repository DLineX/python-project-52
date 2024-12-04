from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse_lazy
from faker import Faker

from .models import User


class TestUsers(TestCase):
    def setUp(self):
        faker_client = Faker()
        self.faker_username = faker_client.user_name()
        self.faker_password = faker_client.password(length=8)
        self.user_client = User.objects.create_user(
            username=self.faker_username,
            password=self.faker_password)
        self.user_client.save()

    def delete_user(self):
        self.user_client.delete()

    def test_correct(self):
        self.client = Client()
        request = self.client.post('/login/',
                                   {'username': self.faker_username,
                                    'password': self.faker_password, },
                                   )
        self.assertEqual(request.status_code, HTTPStatus.FOUND)

    def test_wrong_username(self):
        response = self.client.post('/login/',
                                    {'username': 'wrong',
                                     'password': self.faker_password, },
                                    )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)

    def test_wrong_password(self):
        response = self.client.post('/login/',
                                    {'username': self.faker_username,
                                     'password': 'wrong', },
                                    )
        self.assertFalse(response.status_code == HTTPStatus.FOUND)

    def test(self):
        request = self.client.get(reverse_lazy('login'))
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.test_correct()
        self.test_wrong_username()
        self.test_wrong_password()
