from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'created_at', 'updated_at')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_editable = ('is_staff', 'is_active', 'is_superuser')
    list_per_page = 25
    ordering = ('-created_at',)
