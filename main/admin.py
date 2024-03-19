from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    """
    Admin class for About model. It provides a list of abouts in the admin panel.
    """

    list_display = ('phone',)







