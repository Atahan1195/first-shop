from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib import messages

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):

    """
    This view is used to create an order.
     It includes the following context: title, form, and order.
    """

    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(user=user, phone_number=form.cleaned_data['phone_number'],
                                                     requires_delivery=form.cleaned_data['requires_delivery'],
                                                     delivery_address=form.cleaned_data['delivery_address'],
                                                     payment_on_get=form.cleaned_data['payment_on_get'])
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.total_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError('Not enough products in stock')

                            OrderItem.objects.create(order=order, product=product, name=name, price=price, quantity=quantity)
                            product.quantity -= quantity
                            product.save()

                        cart_items.delete()

                        messages.success(request, 'Order created successfully')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {'name': request.user.name, 'last_name': request.user.last_name}
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Create an order',
        'form': form,
        'order': True
    }
    return render(request, 'create_order.html', context)




