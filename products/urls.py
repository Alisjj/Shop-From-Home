from django.urls import path
from .views import ProductDetailView, SearchResultView

app_name = "products"
urlpatterns = [
    path('<uuid:pk>/', ProductDetailView.as_view(), name="product_details"),
    path('search/', SearchResultView.as_view(), name="search"),
]