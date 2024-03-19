from django.db import models


class About(models.Model):

    """
    This model holds information about the company or organization.
    It includes the following fields: about, address, phone, email, and telegram.
    """

    about = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=255)



