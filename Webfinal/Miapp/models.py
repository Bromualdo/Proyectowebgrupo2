from multiprocessing.sharedctypes import Value
from django.db import models

class Celulares (models.Model):
    marca_celular= models.CharField (max_length=50)
    modelo_celular= models.CharField (max_length=50)
    stock_celular= models.IntegerField ()

class Insumos (models.Model):
    tipo_insumo= models.CharField (max_length=50)
    marca_insumo= models.CharField (max_length=50)
    stock_insumo= models.IntegerField ()

class Hardware (models.Model):
    tipo_hardware= models.CharField (max_length=50) 
    marca_hardware= models.CharField (max_length=50)
    stock_hardware= models.IntegerField()

class Software (models.Model):
    tipo_software= models.CharField (max_length=50) 
    marca_software= models.CharField (max_length=50)
    stock_software= models.IntegerField()



