import django_filters
from .models import Prod

class Prodfilter(django_filters.FilterSet):
    class Meta:
        model=Prod
        fields=("Objectif", "Output", "Date")