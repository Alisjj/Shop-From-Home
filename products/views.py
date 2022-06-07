from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import Q
from cart.forms import AddProductCartForm

from products.models import Category, Item


class CategoryView(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "products/category.html"

    def get_queryset(self):
        return Category.objects.all()

class ProductListView(ListView):
    model = Item
    context_object_name = 'product_list'
    template_name = 'products/home.html'

class ProductDetailView(DetailView):
    model = Item
    context_object_name = 'product'
    form_class = AddProductCartForm()
    template_name = 'products/details.html'

    def get_object(self):
        obj = super().get_object()
        return obj

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inst = self.get_object()
        images = inst.images.all()
        context['form'] = self.form_class
        context['images'] = images
        
        # Add in the publisher
        return context

class SearchResultView(ListView):
    model = Item
    context_object_name = 'product_list'
    template_name = 'products/home.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Item.objects.filter(
            Q(name__icontains=query)
        )
    