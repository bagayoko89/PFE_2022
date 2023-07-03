from django.db import models
from problem.models import Prob

# Create your models here.
class Scrap(models.Model):
    Occurence=models.IntegerField(null=True)
    Date=models.DateField(auto_now=True, null=True)
    heure=models.TimeField(auto_now=True, null=True)
    id_problem = models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)


