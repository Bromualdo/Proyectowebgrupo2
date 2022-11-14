from django.urls import path
from django.contrib.auth.views import LogoutView
from .models import Hardware, Software, Insumos, Celulares
from .views import agregado, celulares, hardware, inicio, insumos, show_celulares,software,buscar_modelo_cel,show_hard, show_insumos,show_soft,nuevin, registro_usuario,eliminar_celular,show_cel_del,editar_celular,show_cel_edit, login_usuario,editar_hardware,eliminar_hardware,show_hard_del,show_hard_edit,show_ins_del,show_ins_edit,editar_insumos,eliminar_insumos,editar_software,show_soft_edit,eliminar_software,show_soft_del   


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
    path ("logout_usuario/", LogoutView.as_view (template_name= "logout.html"), name = "Logout"),
    path('show_cel_del',show_cel_del,name="show_cel_del"),
    path('eliminar_cel/<int:id>',eliminar_celular,name='eliminar_cel'),
    path('show_cel_edit',show_cel_edit,name="show_cel_edit"),
    path('editar_cel/<int:id>',editar_celular,name='editar_cel'),
    path('show_hard_del',show_hard_del,name="show_hard_del"),
    path('eliminar_hard/<int:id>',eliminar_hardware,name='eliminar_hard'),
    path('show_hard_edit',show_hard_edit,name="show_hard_edit"),
    path('editar_hard/<int:id>',editar_hardware,name='editar_hard'),
    path('show_ins_del',show_ins_del,name="show_ins_del"),
    path('eliminar_insumos/<int:id>',eliminar_insumos,name='eliminar_insumos'),
    path('show_ins_edit',show_ins_edit,name="show_ins_edit"),
    path('editar_insumos/<int:id>',editar_insumos,name='editar_insumos'),
    path('show_soft_del',show_soft_del,name="show_soft_del"),
    path('eliminar_software/<int:id>',eliminar_software,name='eliminar_software'),
    path('show_soft_edit',show_soft_edit,name="show_soft_edit"),
    path('editar_software/<int:id>',editar_software,name='editar_software')
    
]
