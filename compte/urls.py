from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns=[
    path('compte/', views.inscription, name='insc'),
    path('acces', views.acces, name='login'),
    path('quitter', views.logoutUser, name='quitter'),
]
