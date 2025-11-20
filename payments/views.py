from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def process_payment(request):
    # integrate with Stripe, PayPal, etc.
    return render(request, 'payments/confirmation.html')
