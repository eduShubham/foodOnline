from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser')
]