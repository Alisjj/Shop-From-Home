from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from products.models import Item

class ProductListView(ListView):
    model = Item
    context_object_name = 'product_list'
    template_name = 'products/home.html'

class ProductDetailView(DetailView):
    model = Item
    context_object_name = 'product'
    template_name = 'products/details.html'