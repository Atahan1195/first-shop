from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User
from orders.admin import OrderTabularAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """
    Admin class for User model to display user details in admin panel and to search user by username,
     email, first_name, last_name. It also includes inlines for Cart and Order models.
    """

    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    inlines = [CartTabAdmin, OrderTabularAdmin]

