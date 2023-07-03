from django.db import models
from machine.models import Machine

# Create your models here.
class Station(models.Model):
    Num_station=models.CharField(primary_key=True, max_length=200)
    id_machine=models.ForeignKey(Machine, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Num_station
