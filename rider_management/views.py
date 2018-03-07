from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rider(request):

	return render(request,'rider.html',{})

def driver(request):

	return render(request,'driver.html',{})		