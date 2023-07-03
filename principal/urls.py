
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('machine.urls')),
    path('', include('station.urls')),
    path('', include('production.urls')),
    path('', include('validation.urls')),
    path('', include('intervention.urls')),
    path('', include('down_time.urls')),
    path('', include('chang_over.urls')),
    path('', include('micro_arrets.urls')),
    path('', include('problem.urls')),
    path('', include('scrap.urls')),
    path('', include('ishikawa.urls')),
    path('', include('whys.urls')),
    path('', include('compte.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
