from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/DOT/DT', views.DT),
    path('choix_machine/choix_suivi<str:pk>/DOT/DT/list', views.list_DT),
]