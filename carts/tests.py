from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cart, Product


class CartModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10)
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=2)

    def test_products_price(self):
        expected_price = 20  # 10(price) * 2(quantity)
        self.assertEqual(self.cart.products_price(), expected_price)

    def test_str_method_with_user(self):
        expected_str = f'Shopping Cart {self.user.username}, | Product {self.product.name} | Quantity {self.cart.quantity}'
        self.assertEqual(str(self.cart), expected_str)

    def test_str_method_without_user(self):
        self.cart.user = None
        self.cart.save()
        expected_str = f'Anonymous Shopping Cart None, | Product {self.product.name} | Quantity {self.cart.quantity}'
        self.assertEqual(str(self.cart), expected_str)

