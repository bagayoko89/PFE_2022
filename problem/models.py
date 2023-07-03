from django.db import models
from station.models import Station

# Create your models here.

class Prob(models.Model):
    id_problem=models.CharField(primary_key=True, max_length=200)
    description=models.CharField(max_length=200, null=True)
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    image4 = models.ImageField(null=True, blank=True, upload_to="images/")
    id_station=models.ForeignKey(Station, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}'. format(self.id_problem)

