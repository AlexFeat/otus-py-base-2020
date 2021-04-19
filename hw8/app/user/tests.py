from django.test import TestCase
from .models import User
from faker import Faker
fake = Faker()

class TestUserView(TestCase):

    def setUp(self):
        self.password = fake.lexify()
        self.user = User.objects.create(
            email=fake.email(),
            name=fake.name(),
            password=User.salt_password(self.password),
            auth_token=User._get_session_token(),
        )

    def test_login(self):
        self.client.post('/login/', {'email': self.user.email, 'password': self.password}, follow=True)
        self.assertIn('fcsid', self.client.cookies)
        response = self.client.get('/me/')
        self.assertIn(self.user.email, response.content.decode(encoding='utf-8'))

    def test_logout(self):
        self.client.post('/login/', {'email': self.user.email, 'password': self.password}, follow=True)
        self.client.post('/logout/', {}, follow=True)
        response = self.client.get('/me/')
        self.assertEqual(response.status_code, 302)

    def test_context(self):
        self.client.post('/login/', {'email': self.user.email, 'password': self.password}, follow=True)
        response = self.client.get('/me/')
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'].id, self.user.id)
