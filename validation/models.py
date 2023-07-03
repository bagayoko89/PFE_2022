from django.db import models
from machine.models import Machine

# Create your models here.
class Val(models.Model):
    Dur = models.IntegerField(null=True)
    Date = models.DateField(auto_now=True, null=True)
    heure = models.TimeField(auto_now=True, null=True)
    commentaire=models.CharField(max_length=200, null=True)
    id_machine = models.ForeignKey(Machine, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} {}'.format(self.Dur, self.id_machine)
