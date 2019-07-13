from django.test import TestCase, Client
from users.models import User


class TestUsers(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creating_a_user_account(self):
        user = User.objects.create_user('jonathanaurugai@gmail.com', 'Jonathan', 'Aurugai', 'test123')
        self.assertIs(user.first_name, 'Jonathan')

    def test_creating_a_user_account_with_no_email(self):
        user = User.objects.create_user(email='', first_name='Jonathan', last_name='Aurugai', password='test123')
        self.assertEqual(user, 'Users must have an Email address')

    def test_creating_a_user_account_with_no_password(self):
        user = User.objects.create_user(email='jonathanaurugai@gmail.com', first_name='Jonathan',
                                        last_name='Aurugai', password='')
        self.assertEqual(user, 'Users must have a Password')

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, 200)
