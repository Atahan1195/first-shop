from django.shortcuts import render
from .models import About


def index(request):

    context: dict = {
        'title': 'Home - Main',
        'content': 'Furniture Store "AYLIN"',
    }
    return render(request, 'main/index.html', context)


def about(request):

    about_all = About.objects.all()

    context = {
        'title': 'Home - About',
        'content': 'About us.',
        'about_all': about_all,
    }
    return render(request, 'main/about.html', context)
