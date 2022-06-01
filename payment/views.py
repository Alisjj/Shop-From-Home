from django.urls import reverse
import json
from orders.models import Order
from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View
import requests

class PaymentVerification(View):
    def get(self, request):
        trxref = request.GET.get('trxref')
        url = f'https://api.paystack.co/transaction/verify/{trxref}'
        headers = {
            'Authorization': f'Bearer {settings.PS_SECRET}',
            'Content-Type': 'application/json'
        }
        resp = json.loads((requests.get(url=url, headers=headers)).content)

        if resp['data']['status'] != "success":
            return redirect(reverse('payment:failed'))

        order_id = str(resp['data']['metadata']['order_id'])
        order = Order.objects.get(id=order_id)
        order.paid=True
        order.save()



        context = {
            'order_id': str(resp['data']['metadata']['order_id'])
        }

        return render(request, "payment/success.html", context=context)