from django.test import TestCase
from django.urls import reverse
from .models import Category, Product


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(slug='test-category', name='Test Category')

    def test_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, 'categories')


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(slug='test-category', name='Test Category')
        self.product = Product.objects.create(
            slug='test-product',
            catalog=self.category,
            name='Test Product',
            description='Test Description',
            price=10.00,
            quantity=5
        )

    def test_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_get_absolute_url(self):
        expected_url = reverse('catalog:product', args=['test-product'])
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    def test_display_id(self):
        self.assertEqual(self.product.display_id(), '0001')  # Assuming it's the first product created

    def test_total_price_without_discount(self):
        self.assertEqual(self.product.total_price(), 10.00)

    def test_total_price_with_discount(self):
        self.product.discount = 20
        self.assertEqual(self.product.total_price(), 8.00)

    def test_verbose_name_plural(self):
        self.assertEqual(Product._meta.verbose_name_plural, 'products')


