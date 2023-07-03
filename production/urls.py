from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/prod', views.prod),
    path('choix_machine/choix_suivi<str:pk>/prod/list', views.list_prod),
    path('proc/suivi<str:pk>/prod', views.graphe),
]