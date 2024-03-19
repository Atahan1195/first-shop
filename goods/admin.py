from django.contrib import admin

from goods.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    """
    Admin class for Category model. It provides a list of categories in the admin panel.
    """

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    """
    Admin class for Product model. It provides a list of products in the admin panel.
    """

    list_display = ['name', 'price', 'quantity', 'discount']
    search_fields = ['name', 'description']
    list_editable = ['discount']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['catalog', 'quantity', 'discount']
    fields = ['name', 'slug', 'catalog', 'description', ('price', 'discount'), 'quantity',  'image']

