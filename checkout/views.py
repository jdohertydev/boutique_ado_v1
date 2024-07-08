from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'sk_test_51PaHy5AUfl3G6KlUihj3vgkO6dgOvC6aVrV1nwQd1Wa6rVJf56ssUCxqDGR9PebxMRHNBiwsfTK1Gu4w7awt4e4H00nOT9zirt',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)