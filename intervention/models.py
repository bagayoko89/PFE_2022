from django.db import models
from station.models import Station

# Create your models here.
class Inter(models.Model):
    Durée = models.IntegerField(null=True)
    Date = models.DateField(auto_now=True, null=True)
    heure = models.TimeField(auto_now=True, null=True)
    commentaire=models.CharField(max_length=200, null=True)
    id_station = models.ForeignKey(Station, null=True, on_delete=models.SET_NULL)

