from django import views
from django.urls import path
from HospitalApp import views
urlpatterns = [
    path('', views.Home, name='home')
]