from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'name': 'Test User',
            'phone_number': '1234567890'
        }

    def test_user_creation(self):
        User = get_user_model()
        user_instance = User.objects.create_user(**self.user_data)
        self.assertEqual(user_instance.username, self.user_data['username'])
        self.assertEqual(user_instance.name, self.user_data['name'])
        self.assertEqual(user_instance.phone_number, self.user_data['phone_number'])
        self.assertTrue(user_instance.is_active)
        self.assertFalse(user_instance.is_staff)
        self.assertFalse(user_instance.is_superuser)

    def test_str_method(self):
        User = get_user_model()
        user_instance = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user_instance), 'testuser')

    def test_verbose_name_plural(self):
        User = get_user_model()
        self.assertEqual(User._meta.verbose_name_plural, 'Users')
