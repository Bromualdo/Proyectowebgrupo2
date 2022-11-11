from multiprocessing.sharedctypes import Value
from django.db import models

class Celulares (models.Model):
    marca= models.CharField (max_length=50)
    modelo= models.CharField (max_length=50)
    stock= models.IntegerField ()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.stock}'

class Insumos (models.Model):
    tipo= models.CharField (max_length=50)
    marca= models.CharField (max_length=50)
    stock= models.IntegerField ()

    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.stock}'


class Hardware (models.Model):
    tipo= models.CharField (max_length=50) 
    marca= models.CharField (max_length=50)
    stock= models.IntegerField()
    
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.stock}'

class Software (models.Model):
    tipo= models.CharField (max_length=50) 
    marca= models.CharField (max_length=50)
    stock= models.IntegerField()
    
    def __str__(self):
        return f'{self.tipo} - {self.marca} - {self.stock}'





