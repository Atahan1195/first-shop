from django.db import models


class About(models.Model):
    about = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=255)



