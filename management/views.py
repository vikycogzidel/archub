from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def apimanage(request):

	return render(request,'api.html',{})