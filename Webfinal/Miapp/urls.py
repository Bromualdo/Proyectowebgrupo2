from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import agregado, celulares, hardware, inicio,insumos, show_celulares,software,buscar_modelo_cel,show_hard,show_insumos,show_soft


urlpatterns = [
    path("", inicio,name='Inicio'),
    path ("lista_hardware/", hardware,name='Hardware'),
    path ("lista_insumos/", insumos,name='Insumos'),
    path ("lista_software/", software,name='Software'),
    path ("lista_celulares/", celulares, name= "Celulares"),
    path ("agregado/", agregado, name = "agregado"),
    path('busqueda_cel/',buscar_modelo_cel ,name="buscar"),
    path('show_cel/',show_celulares,name="show_cel"),
    path('show_hard/',show_hard,name="show_hard"),
    path('show_insumos/',show_insumos,name="show_insumos"),
    path('show_soft/',show_soft,name="show_soft"),
]
