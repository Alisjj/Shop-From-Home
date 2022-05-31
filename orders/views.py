from django.shortcuts import render
from cart.cart import Cart
from django.views.generic import CreateView
from .tasks import order_created
from orders.models import Order, OrderItem


class CreateOrderView(CreateView):
    model = Order
    template_name = "orders/order_create.html"
    success_url = '/orders/created'
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

def created(request):
    return render(request, "orders/created.html")