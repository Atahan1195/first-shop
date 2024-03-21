from django.db import models


class About(models.Model):

    about = models.TextField()

    class Meta:
        verbose_name_plural = 'About'
        verbose_name = 'About'





