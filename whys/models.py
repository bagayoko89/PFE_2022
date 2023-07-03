from django.db import models
from ishikawa.models import *

# Create your models here.

# les 5 whys de la machine
class Why_mac(models.Model):
    why1=models.CharField(max_length=500, null=True)
    why2 = models.CharField(max_length=500, null=True)
    why3 = models.CharField(max_length=500, null=True)
    why4 = models.CharField(max_length=500, null=True)
    why5 = models.CharField(max_length=500, null=True)
    cons=models.ForeignKey(Cause_machine,null=True, on_delete=models.SET_NULL)

# les 5 whys de la matière
class Why_mat(models.Model):
    why1=models.CharField(max_length=500, null=True)
    why2 = models.CharField(max_length=500, null=True)
    why3 = models.CharField(max_length=500, null=True)
    why4 = models.CharField(max_length=500, null=True)
    why5 = models.CharField(max_length=500, null=True)
    cons=models.ForeignKey(Cause_matiere,null=True, on_delete=models.SET_NULL)


#  les 5 whys du milieu

class Why_mi(models.Model):
    why1=models.CharField(max_length=500, null=True)
    why2 = models.CharField(max_length=500, null=True)
    why3 = models.CharField(max_length=500, null=True)
    why4 = models.CharField(max_length=500, null=True)
    why5 = models.CharField(max_length=500, null=True)
    cons=models.ForeignKey(Cause_milieu,null=True, on_delete=models.SET_NULL)


# Les 5 whys Méthode

class Why_me(models.Model):
    why1 = models.CharField(max_length=500, null=True)
    why2 = models.CharField(max_length=500, null=True)
    why3 = models.CharField(max_length=500, null=True)
    why4 = models.CharField(max_length=500, null=True)
    why5 = models.CharField(max_length=500, null=True)
    cons = models.ForeignKey(Cause_methode, null=True, on_delete=models.SET_NULL)

# les 5 whys de la Main_oeuvre

class Why_mai(models.Model):
    why1 = models.CharField(max_length=500, null=True)
    why2 = models.CharField(max_length=500, null=True)
    why3 = models.CharField(max_length=500, null=True)
    why4 = models.CharField(max_length=500, null=True)
    why5 = models.CharField(max_length=500, null=True)
    cons = models.ForeignKey(Cause_main, null=True, on_delete=models.SET_NULL)







