from django.urls import path
from .views import ProductDetailView

app_name = "products"
urlpatterns = [
    path('<uuid:pk>/', ProductDetailView.as_view(), name="product_details"),
]