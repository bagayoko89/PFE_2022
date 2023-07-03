from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/DOT/micro', views.micro),
    path('choix_machine/choix_suivi<str:pk>/DOT/micro/list', views.list_micro),
]