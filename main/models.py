from django.db import models


class About(models.Model):

    """
    This model holds information about the company or organization.
    It includes the following fields: about, address, phone, email, and telegram.
    """

    about = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    address = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)



