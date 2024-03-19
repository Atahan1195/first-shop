from django.urls import path
from .views import cart_add, cart_remove, cart_change

app_name = 'carts'

urlpatterns = [
    path('cart_add/', cart_add, name='add'),
    path('cart_remove/', cart_remove, name='remove'),
    path('cart_change/', cart_change, name='change'),
]

