from django.db import models
from django.urls import reverse


class Category(models.Model):

    """
    This model is for the categories of products. It has a slug field for the URL,
     and a name field for the category name. It also has a method to display the category name.
    """

    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):

    """
    This model is for the products. It has a slug field for the URL, a ForeignKey to the Category model,
     a name field for the product name, a description field for the product description,
      a price field for the product price, an image field for the product image,
       a quantity field for the product quantity, a discount field for the product discount,
        and a position field for the product position. It also has a method to get the absolute URL of the product,
         a method to display the product ID, and a method to calculate the total price of the product.
    """

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
