from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dash(request):

	return render(request,'dashboard.html',{})