from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Category, Product
from .utils import q_search


def catalog(request, category_slug=None):

    """
    Catalog view function that displays a list of products in a category.
        The function takes a request and a category slug as input.
         The function gets the category with the given slug from the database.
        If the category slug is 'all', the function gets all products from the database.
         If the category slug is not 'all', the function gets all products in the category from the database.
          The function gets the page number from the request. The function gets the on_sale parameter from the request.
           The function gets the order_by parameter from the request.
            The function gets the query parameter from the request.
             If the on_sale parameter is True, the function filters the products to only include products that
              are on sale.
              If the order_by parameter is not 'default', the function orders the products by the given parameter.
               If the query parameter is not None, the function searches for products that match the query.
                The function uses the q_search function to search for products that match the query.
                 The function paginates the products and returns a list of products for the current page.
                  The function returns a render of the catalog.html template with the list of products
                   for the current page.
                    The function is used in the catalog view to display a list of products in a category.
                     The function is also used in the search view to display a list of products that match the query.
                      The function is also used in the home view to display a list of products in a category.
                       The function is also used in the product detail view to display a list of related products.
                        The function is also used in the product detail view to display a list of products
                         in the category.
    :param request: request
    :param category_slug: str
    :return: render
    """

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 9)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'slag_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, products_slug):

    """
    Product view function that displays a product detail.
        The function takes a request and a product slug as input.
         The function gets the product with the given slug from the database.
          The function returns a render of the product.html template with the product detail.
           The function is used in the product detail view to display a product detail.
            The function is also used in the search view to display a product detail.
             The function is also used in the cart view to display a product detail.
              The function is also used in the catalog view to display a product detail.
               The function is also used in the home view to display a product detail.
    :param request: request
    :param products_slug: str
    :return: render
    """

    products = Product.objects.get(slug=products_slug)
    context = {
        'product': products,
    }
    return render(request, 'goods/product.html', context=context)


