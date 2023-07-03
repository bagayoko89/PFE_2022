import django_filters
from .models import Scrap

class Scrapfilter(django_filters.FilterSet):
    class Meta:
        model=Scrap
        fields=('Date',)