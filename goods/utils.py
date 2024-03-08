from goods.models import Product
from django.db.models import Q


def q_search(query):
    if query.isdigit and len(query) <= 4:
        return Product.objects.filter(id=query)
    return Product.objects.filter(Q(description__search=query)) | Product.objects.filter(Q(name__search=query))

    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_objects = Q()
    #
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    #
    # return Product.objects.filter(q_objects)

