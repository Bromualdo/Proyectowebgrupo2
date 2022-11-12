from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import agregado, celulares, hardware, inicio, insumos, show_celulares,software,buscar_modelo_cel,show_hard, show_insumos,show_soft,nuevin, registro_usuario,eliminar_celular,show_cel_del,editar_celular,show_cel_edit, login_usuario


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
    path('nuevin/',nuevin),
    path('formulario_registro_usuario/', registro_usuario, name ="Registro"),
    path ("login_usuario/", login_usuario, name ="Login"),
    path('show_cel_del',show_cel_del,name="show_cel_del"),#template donde se eliminan los celulares
    path('eliminar_cel/<int:id>',eliminar_celular,name='eliminar_cel'),#eliminacion deregistros de celulares
    path('show_cel_edit',show_cel_edit,name="show_cel_edit"),#template donde se eliminan los celulares
    path('editar_cel/<int:id>',editar_celular,name='editar_cel')
]
