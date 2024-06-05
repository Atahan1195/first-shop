from django.db import models


class About(models.Model):

    phone = models.CharField(max_length=15, blank=True, null=True)
    about = models.TextField(max_length=200000, blank=True, null=True)
    address = models.URLField(max_length=200, blank=True, null=True)
    telegram = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'About'
        verbose_name = 'About'
