from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def erider(request):

	return render(request,'editrider.html',{})