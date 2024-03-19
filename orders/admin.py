from django.contrib import admin
from .models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):

    """
    This class is used to display the OrderItem model in the admin panel.
    It includes the following fields: product, name, price, and quantity.
    """

    model = OrderItem
    fields = ('product', 'name', 'price', 'quantity')
    search_fields = ('product', 'name')
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    """
    This class is used to display the OrderItem model in the admin panel.
    It includes the following fields: order, product, name, price, and quantity.
    """

    list_display = ('order', 'product', 'name', 'price', 'quantity')
    search_fields = ('order', 'product', 'name')


class OrderTabularAdmin(admin.TabularInline):

    """
    This class is used to display the Order model in the admin panel.
    It includes the following fields: requires_delivery, payment_on_get, is_paid, status, and created_timestamp.
    """

    model = Order
    fields = ('requires_delivery', 'payment_on_get', 'is_paid', 'status', 'created_timestamp')
    search_fields = ('requires_delivery', 'payment_on_get', 'is_paid', 'status')
    readonly_fields = ('created_timestamp',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_timestamp', 'requires_delivery', 'payment_on_get',
                    'is_paid', 'status')
    search_fields = ('id',)
    readonly_fields = ('created_timestamp',)
    list_filter = ('requires_delivery', 'payment_on_get', 'is_paid', 'status')
    inlines = (OrderItemTabularAdmin,)
