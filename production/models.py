from django.db import models
from machine.models import Machine

# Create your models here.
class Prod(models.Model):
    Objectif=models.IntegerField(null=True)
    Output=models.IntegerField(null=True)
    Date=models.DateField(auto_now=True, null=True)
    heure=models.TimeField(auto_now=True, null=True)
    id_machine = models.ForeignKey(Machine, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} {}'. format(self.Objectif, self.Output)

