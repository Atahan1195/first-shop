from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """
    It is a model for user. It is used to store the user details.
    """

    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

