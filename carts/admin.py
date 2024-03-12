from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'session_key', 'created_timestamp')
    search_fields = ('user', 'product', 'session_key')
