import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
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

        resp[''] 

        return HttpResponse(f'<h1>{resp}</h1>')