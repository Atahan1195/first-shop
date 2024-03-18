from django.db import models
from goods.models import Product
from users.models import User


class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='quantity')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    objects = CartQuerySet().as_manager()

    def products_price(self):
        return round(self.product.total_price() * self.quantity, 2)

    def __str__(self):
        return f'Shopping Cart {self.user.username}, | Product {self.product.name} | Quantity {self.quantity}'

