from django.test import TestCase
from .models import About


class AboutModelTestCase(TestCase):
    def setUp(self):
        self.about_data = {
            'about': 'Some information about us',
            'address': '123 Main St, City, Country',
            'phone': '1234567890',
            'email': 'example@example.com',
            'telegram': '@example'
        }

    def test_about_creation(self):
        about_instance = About.objects.create(**self.about_data)
        self.assertEqual(about_instance.about, self.about_data['about'])
        self.assertEqual(about_instance.address, self.about_data['address'])
        self.assertEqual(about_instance.phone, self.about_data['phone'])
        self.assertEqual(about_instance.email, self.about_data['email'])
        self.assertEqual(about_instance.telegram, self.about_data['telegram'])
