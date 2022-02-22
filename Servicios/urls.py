from django import views
from django.urls import path, include
from Servicios import views

urlpatterns = [
    path('', views.Servicios),
]