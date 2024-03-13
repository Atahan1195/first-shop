from django.urls import path
from .views import cart_add, cart_remove, cart_change

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>/', cart_add, name='add'),
    path('cart_remove/<int:cart_id>/', cart_remove, name='remove'),
    path('cart_change/<slug:product_slug>/', cart_change, name='change'),
]

