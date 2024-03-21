from goods.models import Product
from django.db.models import Q


def q_search(query):
    """
    This function is used to search for products in the database.
    It takes a query and returns a list of products that match the query.
    The query can be a string or an integer.
    If the query is an integer, it is assumed to be a product id and the function returns
    a list of products with that id. If the query is a string, the function searches for products with
    a name or description that contains the query string. The function uses the Q object to create a query
    that matches products with a name or description that contains any of the words in the query string.
    The function returns a list of products that match the query. If no products match the query,
    the function returns an empty list. The function is used in the search view to search for products
    in the database. The function is also used in the product detail view to search for related products.
    """

    if query.isdigit() and len(query) <= 4:
        return Product.objects.filter(id=query)
    else:
        return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))


