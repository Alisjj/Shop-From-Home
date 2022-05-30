from decimal import Decimal
from django.conf import settings
from products.models import Item

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, item, quantity=1, override_quantity=False):
        """
        Add/Update the cart 
        """

        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price)
            }

        if override_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)

        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item

        for product in cart.values():
            product['price'] = Decimal(product['price'])
            product['total_price'] = product['price'] * product['quantity']
            yield product

    def __len__(self):
        return sum(product['quantity'] for product in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(product['price']) * product['quantity'] for product in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
