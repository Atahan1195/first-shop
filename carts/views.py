from django.http import JsonResponse
from django.template.loader import render_to_string

from goods.models import Product
from .models import Cart
from .utils import get_user_carts


def cart_add(request):

    """
    Add product to cart view function that adds a product to the cart.
     The function takes a request and a product id as input.
      The function gets the product with the given id from the database.
       If the user is authenticated, the function gets the user's cart from the database.
        If the user has a cart with the given product, the function increases the quantity of the product
         in the cart by one. If the user does not have a cart with the given product,
          the function creates a new cart with the given product and a quantity of one.
           If the user is not authenticated, the function creates a new session and gets the cart with
            the given product from the database. If the user has a cart with the given product,
             the function increases the quantity of the product in the cart by one.
              If the user does not have a cart with the given product,
               the function creates a new cart with the given product and a quantity of one.
                The function returns a JsonResponse with a message and the cart items html.
                 The message is "Item added to cart" and the cart items html is the html for the cart items.
                  The function is used in the product detail view to add a product to the cart.
                   The function is also used in the cart view to add a product to the cart.
    :param request: request
    :return: JsonResponse
    """

    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)

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
        if not request.session.session_key:
            request.session.create()
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/included_cart.html', {"carts": user_cart}, request=request)

    response_data = {
        "message": "Item added to cart",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    """
    Remove product from cart view function that removes a product from the cart.
     The function takes a request and a cart id as input.
      The function gets the cart with the given id from the database.
       The function gets the quantity of the product in the cart.
        The function deletes the cart from the database.
         The function gets the user's cart from the database.
          The function renders the cart items html with the user's cart.
           The function returns a JsonResponse with a message, the cart items html, and the quantity deleted.
            The message is "Item removed from cart" and the cart items html is the html for the cart items.
             The quantity deleted is the quantity of the product that was removed from the cart.
              The function is used in the cart view to remove a product from the cart.
               The function is also used in the cart view to remove a product from the cart.
    :param request: request
    :return: JsonResponse
    """

    cart_id = request.POST.get('cart_id')

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/included_cart.html', {"carts": user_cart}, request=request)

    response_data = {
        "message": "Item removed from cart",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string('includes/included_cart.html', {"carts": cart}, request=request)

    response_data = {
        "message": "Cart updated",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)
