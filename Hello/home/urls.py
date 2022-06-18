from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('nature', views.nature, name='nature'),
    path('car', views.car, name='car'),
    path('cuteanimals', views.cuteanimals, name='cuteanimals'),
    path('common', views.common, name='common'),
    
    path('colors', views.colors, name='colors'),
    

    path('contact', views.contact, name='contact'),
]
