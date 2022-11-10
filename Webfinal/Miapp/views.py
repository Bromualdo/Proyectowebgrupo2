from http.client import HTTPResponse
from this import d
from urllib.request import Request
from django.shortcuts import render, redirect
from django.template import Context, Template
from Miapp.forms import Formulario_Insumos, Formulario_celulares, Formulario_hardware, Formulario_software
from .models import Celulares, Insumos,Hardware,Software
from .forms import UserRegisterForm

# Create your views here.

def inicio (request):
    return render(request,"inicio.html")

def nuevin(request):
    return render(request,'nuevin.html')

def celulares (request):
    if request.method == "POST":
        mi_formulario = Formulario_celulares (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Celulares (marca=data ['marca'], modelo= data ['modelo'], stock= data ['stock'])
            formulario.save()
            return redirect ("show_cel")
    else:
            mi_formulario = Formulario_celulares ()
    return render (request, "lista_celulares.html", {'mi_formulario': mi_formulario})
    

def hardware (request):
    if request.method == "POST":
        mi_formulario = Formulario_hardware (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Hardware (tipo=data ['tipo'], marca = data ['marca'], stock= data ['stock'])
            formulario.save()
            return redirect ("show_hard")
    else:
            mi_formulario = Formulario_hardware ()
    return render (request, "lista_hardware.html", {'mi_formulario': mi_formulario})

def software (request):
    if request.method == "POST":
        mi_formulario = Formulario_software (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Software (tipo=data ['tipo'], marca= data ['marca'], stock= data ['stock'])
            formulario.save()
            return redirect ("show_soft")
    else:
            mi_formulario = Formulario_software ()
    return render (request, "lista_software.html", {'mi_formulario': mi_formulario})
    

def insumos (request):
    if request.method == "POST":
        mi_formulario = Formulario_Insumos (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Insumos (tipo=data ['tipo'], marca= data ['marca'], stock= data ['stock'])
            formulario.save()
            return redirect ("show_insumos")
    else:
            mi_formulario = Formulario_Insumos ()
    return render (request, "lista_insumos.html", {'mi_formulario': mi_formulario})
    

def agregado (request):
    return render (request, "agregado.html")

def formulario_insumo (request):
    if request.method == "POST":
        mi_formulario = Formulario_Insumos (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Insumos (tipo=data ['tipo'], marca= data ['marca'], stock= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_Insumos ()
    return render (request, "formulario_insumo.html", {'mi_formulario': mi_formulario})

def formulario_software (request):
    if request.method == "POST":
        mi_formulario = Formulario_software (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Software (tipo=data ['tipo'], marca= data ['marca'], stock= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_software ()
    return render (request, "formulario_software.html", {'mi_formulario': mi_formulario})

def buscar_modelo_cel(request):
        if request.GET['busqueda']:
            modelo_buscado=request.GET['busqueda']
            celulares=Celulares.objects.filter(modelo__icontains=modelo_buscado)
        
            return render(request,"busqueda_cel.html",{"celulares":celulares,"modelo":modelo_buscado,})
        else:
            respuesta="usted ha ingresado datos en blanco, intente de nuevo"
        return render(request,'busqueda_cel.html',{"respuesta":respuesta})
   
   
   
def show_celulares(request):
    lista = Celulares.objects.all()    
    return render(request, "show_cel.html",{"Celulares": lista} )
def show_insumos(request):
    lista = Insumos.objects.all()    
    return render(request, "show_insumos.html",{"Insumos": lista} )
def show_soft(request):
    lista = Software.objects.all()    
    return render(request, "show_soft.html",{"Software": lista} )
def show_hard(request):
    lista = Hardware.objects.all()    
    return render(request, "show_hard.html",{"Hardware": lista} )
    

def registro_usuario(request):

    if request.method == 'POST':
    
        formulario_registro_usuario = UserRegisterForm(request.POST)
    
        if formulario_registro_usuario.is_valid():
	
            nombre_usuario= formulario_registro_usuario.cleaned_data["username"] 
            
            formulario_registro_usuario.save()
	        
            return render(request, "inicio2.html", {"mensaje": f'El usuario {nombre_usuario} ha sido creado con éxito'})
	    
        else:
	    
            return render(request, "inicio2.html", {"mensaje": f'Error al crear usuario'})
    else:
        formulario_registro_usuario = UserRegisterForm()
	    
        return render(request, "formulario_registro_usuario.html", {"formulario_registro": formulario_registro_usuario})
    



