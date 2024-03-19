from carts.models import Cart


def get_user_carts(request):
    """
    Get user carts
    :param request: request
    :return: Cart
    """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')
    else:
        return Cart.objects.filter(session_key=request.session.session_key).select_related('product')