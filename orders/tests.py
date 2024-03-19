from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderItem


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.order = Order.objects.create(
            user=self.user,
            phone_number='1234567890',
            requires_delivery=True,
            delivery_address='Test Address',
            payment_on_get=False,
            is_paid=False,
            status='in processing'
        )

    def test_str_method(self):
        expected_str = f'Order {self.order.id} by {self.user}'
        self.assertEqual(str(self.order), expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(Order._meta.verbose_name_plural, 'Orders')


class OrderItemModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.order = Order.objects.create(
            user=self.user,
            phone_number='1234567890',
            requires_delivery=True,
            delivery_address='Test Address',
            payment_on_get=False,
            is_paid=False,
            status='in processing'
        )
        self.product_price = 10.00
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=None,
            name='Test Product',
            price=self.product_price,
            quantity=2
        )

    def test_str_method(self):
        expected_str = f'Order item {self.order_item.id} for {self.order}'
        self.assertEqual(str(self.order_item), expected_str)

    def test_products_price(self):
        expected_price = self.product_price * 2
        self.assertEqual(self.order_item.products_price(), expected_price)

    def test_verbose_name_plural(self):
        self.assertEqual(OrderItem._meta.verbose_name_plural, 'Order items')

