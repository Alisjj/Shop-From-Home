from django.test import Client
from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Item

class Cart(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user( # new
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.item = Item.objects.create(
            name='gown',
            description='this is a wedding gown',
            price='250.00',
        )

        self.request = {
            'item': self.item,
            'quantity': 1,
            'override': False
        }

    def test_cart(self):
        c = Client()
        response = c.post(f'/cart/add/{self.item.id}', data=self.request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'self.item.name')