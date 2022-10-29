from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import celulares, hardware, inicio, insumos,software


urlpatterns = [
    path("", inicio,name='Inicio'),
    path ("lista_celulares/", celulares,name='Celulares'),
    path ("lista_hardware/", hardware,name='Hardware'),
    path ("lista_insumos/", insumos,name='Insumos'),
    path ("lista_software/", software,name='Software'),
]
