from django.urls import path
from .views import CartDetail, add_cart, remove_cart

app_name="cart"

urlpatterns = [
    path('', CartDetail.as_view(), name="cart_detail"),
    path('add/<uuid:item_id>/', add_cart, name="cart-add"),
    path('remove/<uuid:item_id>/', remove_cart, name="cart-remove"),
    ]