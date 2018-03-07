from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def site(request):
	return render(request,'sitesetting.html',{})

