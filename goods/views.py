from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, Product
from .utils import q_search


def catalog(request, categories_slug=None, categories_product=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if categories_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(catalog__slug=categories_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'slag_url': categories_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, products_slug):
    products = Product.objects.get(slug=products_slug)
    context = {
        'product': products,
    }
    return render(request, 'goods/product.html', context=context)


