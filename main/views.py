from django.shortcuts import render
from .models import About


def index(request):

    """
    This view returns the main page of the website.
    It includes the following context: title and content.
    """

    context: dict = {
        'title': 'Home - Main',
        'content': 'Furniture Store "AYLIN"',
    }
    return render(request, 'main/index.html', context)


def about(request):

    """
    This view returns the about page of the website.
    It includes the following context: title, content, and about_all.
    """

    about_all = About.objects.all()

    context = {
        'title': 'Home - About',
        'content': 'About us.',
        'about_all': about_all,
    }
    return render(request, 'main/about.html', context)
