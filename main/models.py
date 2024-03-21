from django.db import models


class About(models.Model):

    phone = models.CharField(max_length=15)
    about = models.TextField()
    address = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = 'About'
        verbose_name = 'About'





