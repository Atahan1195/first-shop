from django import template

from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    """
    Get user carts
    :param request: request
    :return: get_user_carts
    """
    return get_user_carts(request)










