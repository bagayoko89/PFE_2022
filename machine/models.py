from django.db import models

# Create your models here.

class Machine(models.Model):
    nom=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom
