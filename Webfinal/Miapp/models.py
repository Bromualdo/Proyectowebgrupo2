from multiprocessing.sharedctypes import Value
from django.db import models

class Celulares (models.Model):
    marca= models.CharField (max_length=50)
    modelo= models.CharField (max_length=50)
    stock= models.IntegerField ()

class Insumos (models.Model):
    tipo= models.CharField (max_length=50)
    marca= models.CharField (max_length=50)
    stock= models.IntegerField ()

class Hardware (models.Model):
    tipo= models.CharField (max_length=50) 
    marca= models.CharField (max_length=50)
    stock= models.IntegerField()

class Software (models.Model):
    tipo= models.CharField (max_length=50) 
    marca= models.CharField (max_length=50)
    stock= models.IntegerField()



