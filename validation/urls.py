from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/DOT/val', views.val),
    path('choix_machine/choix_suivi<str:pk>/DOT/val/list', views.list_val),
    path('proc/suivi<str:pk>/DT', views.graphe),
]