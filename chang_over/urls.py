from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/DOT/chang', views.chang),
    path('choix_machine/choix_suivi<str:pk>/DOT/chang/list', views.list_chang),
]