from django.contrib import admin
from .models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    search_fields = ('product', 'created_timestamp', 'quantity')
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    search_fields = ('user', 'product', 'created_timestamp')
    list_filter = ('user', 'created_timestamp')


