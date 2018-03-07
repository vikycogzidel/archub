from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pending(request):

	return render(request,'payment_details/pending_payment.html',{})

def paid(request):

	return render(request,'payment_details/paid_payment.html',{})

