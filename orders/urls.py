from django.urls import path
from .views import CreateOrderView, created, OrderHistory

app_name = "orders"
urlpatterns = [
    path("create/", CreateOrderView.as_view(), name="create-order"),
    path("created/", created, name="created"),
    path("orders-history/", OrderHistory.as_view(), name="order-history"),
]