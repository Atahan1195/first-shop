from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegisterForm, ProfileForm


def login(request):

    """
    It is used to authenticate the user. It is used to login the user. It is used to redirect the user to the next page.
    :param request: request
    :return: render
    """

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, 'You are logged in')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def register(request):

    """
    It is used to register the user. It is used to create a new user. It is used to redirect the user to the next page.
    :param request: request
    :return: render
    """

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f'{user.username}, You are registered')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):

    """
    It is used to display the user profile. It is used to update the user profile. It is used to display the user orders
    :param request: request
    :return: render
    """

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (Order.objects.filter(user=request.user)
              .prefetch_related(
        Prefetch("orderitem_set",
                 queryset=OrderItem.objects.select_related('product'),
                 )
    )
              .order_by('-id')
              )
    context = {
        'title': 'Profile',
        'form': form,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context=context)


@login_required
def logout(request):

    """
    It is used to logout the user. It is used to redirect the user to the main page.
    :param request: request
    :return: HttpResponseRedirect
    """

    messages.success(request, 'You are logged out')
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')
