from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from products.models import Item, Review
from .views import ProductListView

class HomePageTest(TestCase):

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

        self.reviews = Review.objects.create(
            item = self.item,
            author = self.user,
            review = "Amazing!!!!"
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

    def test_product_detail_view(self):
        response = self.client.get(self.item.get_absolute_url())
        no_response = self.client.get('/products/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Amazing!!!!')
        self.assertContains(response, 'gown')
        self.assertTemplateUsed(response, 'products/details.html')