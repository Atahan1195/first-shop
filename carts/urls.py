from django.urls import path
from .views import cart_add, cart_remove, cart_change

app_name = 'carts'

urlpatterns = [
    path('cart_add/<int:product_id>/', cart_add, name='add'),
    path('cart_remove/<int:product_id>/', cart_remove, name='remove'),
    path('cart_change/<int:product_id>/', cart_change, name='change'),
]

