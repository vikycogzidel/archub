from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def edriver(request):

	return render(request,'editdriver.html',{})