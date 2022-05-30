from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.decorators.http import require_POST
from products.models import Item
from .cart import Cart
from .forms import AddProductCartForm
from django.views.generic.edit import FormView

@require_POST
def add_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = AddProductCartForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            item=item, quantity=cd['quantity'], override_quantity=cd['override']
        )

    return redirect('cart:cart_detail')

@require_POST
def remove_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')

class CartDetail(View):
    template_name = 'cart/cart_detail.html'

    def get(self, request):
        cart = Cart(request)
        for product in cart:
            product['update_quantity_form'] = AddProductCartForm(initial={
            'quantity': product['quantity'],
            'override': True})
        
        print("This is" + product.item for product in cart)
        return render(request, self.template_name, {'cart': cart})
