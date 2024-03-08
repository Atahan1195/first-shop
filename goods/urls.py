from django.urls import path
from .views import catalog, product

app_name = 'goods'

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:categories_slug>/', catalog, name='index'),
    path('products/<slug:products_slug>/', product, name='product'),
]