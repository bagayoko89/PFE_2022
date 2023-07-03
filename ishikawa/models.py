from django.db import models
from problem.models import Prob

# Create your models here.

# Création des 5M de ISHIKAWA
class Macine(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    id_problem=models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)

class Matière(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    id_problem=models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)

class Milieu(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    id_problem=models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)

class Méthode(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    id_problem=models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)


class Main_oeuvre(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    id_problem=models.ForeignKey(Prob, null=True, on_delete=models.SET_NULL)


# Création des causes

class Cause_machine(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    cause=models.ForeignKey(Macine,null=True, on_delete=models.SET_NULL)

class Cause_matiere(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    cause=models.ForeignKey(Matière,null=True, on_delete=models.SET_NULL)

class Cause_milieu(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    cause=models.ForeignKey(Milieu,null=True, on_delete=models.SET_NULL)

class Cause_methode(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    cause=models.ForeignKey(Méthode,null=True, on_delete=models.SET_NULL)

class Cause_main(models.Model):
    id=models.CharField(primary_key=True,max_length=200)
    nom=models.CharField(max_length=200, null=True)
    cause=models.ForeignKey(Main_oeuvre,null=True, on_delete=models.SET_NULL)


