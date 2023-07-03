from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='accueil'),
    path('choix_machine/', views.choix_machine, name='mac'),
    path('choix_machine/choix_suivi<str:pk>', views.choix_suivi, name='suivi'),
    path('choix_machine/choix_suivi<str:pk>/DOT/', views.DOT),
    path('opt/', views.opt, name='option'),
    path('opt/ajm', views.ajout_machine),
    path('opt/ajs', views.ajout_station),
    path('opt/ajd', views.ajout_problem),
    path('proc/', views.choix_process,name='process'),
    path('proc/suivi<str:pk>', views.suivi_proc, name='sui'),
    path('RM/',views.RM, name='reac'),
    path('RM/choix<str:pk>', views.RM_choix, name='chx'),
    path('RM/choix<str:pk>/<str:pt>', views.prob_suivi, name='liste'),
    path('RM/choix<str:pk>/<str:pt>/analyse', views.analyse, name='rm'),
    path('RM/choix<str:pk>/<str:pt>/analyse/whymac<str:pr>', views.why_mac, name='whmac'),
    path('RM/choix<str:pk>/<str:pt>/analyse/whymat<str:pr>', views.why_mat, name='whmat'),
    path('RM/choix<str:pk>/<str:pt>/analyse/whymil<str:pr>', views.why_mil, name='whmil'),
    path('RM/choix<str:pk>/<str:pt>/analyse/whyme<str:pr>', views.why_met, name='whme'),
    path('RM/choix<str:pk>/<str:pt>/analyse/whymai<str:pr>', views.why_mai, name='whmai'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)