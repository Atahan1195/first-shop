from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Category, Product


def index(request):

    context: dict = {
        'title': 'Home - Main',
        'content': 'Furniture Store "AYLIN"',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Home - About',
        'content': 'About us.',
        'text_on_page': 'This is a furniture store "HOME". We have a wide range of furniture for every taste. '
                        'We are waiting for you in our store.'
    }
    return render(request, 'main/about.html', context)
