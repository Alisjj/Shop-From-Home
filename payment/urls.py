from django.urls import path
from .views import PaymentVerification

app_name = "payment"
urlpatterns = [
    path('', PaymentVerification.as_view(), name="payment-verification"),
]