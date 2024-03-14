from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from goods.models import Product
from .models import Cart
from .templatetags.carts_tags import user_carts
from .utils import get_user_cart


def cart_add(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, product=product)

        if 'action' in request.POST:
            action = request.POST['action']

            if action == 'increment':
                cart.quantity += 1
            elif action == 'decrement':
                if cart.quantity > 1:
                    cart.quantity -= 1
            cart.save()

    return redirect(request.META['HTTP_REFERER'])






























