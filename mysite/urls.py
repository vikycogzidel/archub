"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from new_app.views import login
from dashboard.views import dash
from settings_app.views import site
from accounts.views import changepassword
from rider_management.views import driver,rider
from editrider.views import erider
from editdriver.views import edriver
from management.views import apimanage
from payment.views import pending
from payment.views import paid
urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^$', login, name='login'),
    url(r'^dashboard/$', dash, name='dashboard'),
    url(r'^site/$', site, name='site'),   
    url(r'^changepassword/$', changepassword, name='changepassword'),
    url(r'^driver/$', driver, name='driver'),
    url(r'^rider/$', rider, name='rider'),
    url(r'^editrider/$', erider, name='editrider'),
    url(r'^editdriver/$', edriver, name='editdriver'),
    url(r'^apimanage/$', apimanage, name='apimanage'),
    url(r'^paid/$', paid, name='paid'),
    url(r'^pending/$', pending, name='pending'),
]       
