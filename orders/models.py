from django.db import models


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, blank=True, null=True,
                             default=None, verbose_name='User')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created timestamp')
    phone_number = models.CharField(max_length=20, verbose_name='Phone number')
    requires_delivery = models.BooleanField(default=False, verbose_name='Requires delivery')
    delivery_address = models.TextField(blank=True, verbose_name='Delivery address')
    payment_on_get = models.BooleanField(default=False, verbose_name='Payment on get')
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')
    status = models.CharField(max_length=50, verbose_name='Order Status', default='in processing')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'order'

    def __str__(self):
        return f'Order {self.id} by {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey('goods.Product', on_delete=models.SET_DEFAULT, null=True,
                                verbose_name='Product', default=None)
    name = models.CharField(max_length=255, verbose_name='Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created timestamp')

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
        db_table = 'order_item'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.total_price() * self.quantity, 2)

    def __str__(self):
        return f'Order item {self.id} for {self.order}'
