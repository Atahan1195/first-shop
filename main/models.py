from django.db import models


class About(models.Model):

    """
    This model holds information about the company or organization.
    It includes the following fields: about, address, phone, email, facebook, instagram, and telegram.
    """
    about = models.TextField()

    class Meta:
        verbose_name_plural = 'About'
        verbose_name = 'About'





