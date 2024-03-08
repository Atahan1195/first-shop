from django.contrib import admin

from goods.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'is_visible', 'catalog', 'position']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

