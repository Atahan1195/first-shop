from django.db import models


class About(models.Model):

    """
    This model holds information about the company or organization.
    It includes the following fields: about, address, phone, email, facebook, instagram, and telegram.
    """

    about = models.TextField(blank=True, max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    address = models.URLField(blank=True, max_length=255)
    facebook = models.URLField(blank=True, max_length=255)
    email = models.EmailField(blank=True, max_length=255)
    instagram = models.URLField(blank=True, max_length=255)
    telegram = models.URLField(blank=True, max_length=255)

    class Meta:
        verbose_name_plural = 'About'
        verbose_name = 'About'





