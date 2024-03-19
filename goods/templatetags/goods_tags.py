from django.utils.http import urlencode

from goods.models import Category
from django import template

register = template.Library()


@register.simple_tag
def tag_categories():

    """
    Get all categories from Category model
    :return: Category
    """

    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):

    """
    Change params in url query string
    :param context: context
    :param kwargs: kwargs
    :return: urlencoded query
    """

    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


