import json
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.sites.models import Site
import requests
from cart.cart import Cart
from django.views.generic import CreateView
from django.views import View
from .tasks import order_created
from orders.models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "orders/order_create.html"
    
    fields = [
        'first_name',
        'last_name',
        'email',
        'address',
        'apartment',
        'city',
        'country',
        'state_province',
        'postal_code',
        ]

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        amount = int(cart.get_total_price())
        email = form.cleaned_data['email']
        headers = {
            'Authorization': f'Bearer {settings.PS_SECRET}',
            'Content-Type': 'application/json'
        }

        current_site = Site.objects.get_current()
        

        data = {
            'amount': amount * 100,
            'email': email,
            'callback_url': f'https://{current_site.domain}/payment',
            'metadata': {
                'order_id': str(order.id)
            }
        }

        
        url = "https://api.paystack.co/transaction/initialize"
        resp = requests.post(url=url, json=data, headers=headers)
        respo = json.loads(resp.content)
        self.success_url = str(respo['data']['authorization_url'])
        print(self.success_url)


        for product in cart:
            OrderItem.objects.create(
                order=order, item=product['item'], 
                price=product['price'], quantity=product['quantity']
                )

        cart.clear()
        order_created.delay(order.id)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context

# class CreateCheckoutSession(View):
#     def post(self, request, *args, **kwargs):
        

def created(request):
    return render(request, "orders/created.html")