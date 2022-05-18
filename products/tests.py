from re import L
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from products.models import Item
from .views import ProductListView

class HomePageTest(TestCase):

    def setUp(self):
        self.item = Item.objects.create(
        name='gown',
        description='this is a wedding gown',
        price='250.00',
        )

    def test_item_listins(self):
        self.assertEqual(f'{self.item.name}', 'gown')
        self.assertEqual(f'{self.item.description}', 'this is a wedding gown')
        self.assertEqual(f'{self.item.price}', '250.00')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'gown')
        self.assertTemplateUsed(response, 'products/home.html')

    def test_book_detail_view(self):
        response = self.client.get(self.item.get_absolute_url())
        no_response = self.client.get('/products/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'gown')
        self.assertTemplateUsed(response, 'products/details.html')