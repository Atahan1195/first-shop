from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):

    slug = models.SlugField(max_length=100, unique=True)
    catalog = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', args=[self.slug])

    def display_id(self):
        return f'{self.id:04}'

    def total_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price
