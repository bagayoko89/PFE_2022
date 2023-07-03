from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/DOT/inter', views.inter),
    path('choix_machine/choix_suivi<str:pk>/DOT/inter/list', views.list_inter),
]