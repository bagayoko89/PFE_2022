from django.urls import path, include
from . import views

urlpatterns=[
    path('choix_machine/choix_suivi<str:pk>/scrap', views.scrap),
    path('choix_machine/choix_suivi<str:pk>/scrap/list', views.list_scrap),
    path('proc/suivi<str:pk>/scrap', views.graphe),
]