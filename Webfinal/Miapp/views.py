from http.client import HTTPResponse
from this import d
from urllib.request import Request
from django.shortcuts import render, redirect
from django.template import Context, Template
from Miapp.forms import Formulario_Insumos, Formulario_celulares, Formulario_hardware, Formulario_software
from .models import Celulares, Insumos,Hardware,Software

# Create your views here.

def inicio (request):
    return render(request,"inicio.html")


def celulares (request):
    if request.method == "POST":
        mi_formulario = Formulario_celulares (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            formulario = Celulares (marca_celular=data ['marca'], modelo_celular= data ['modelo'], stock_celular= data ['stock'])
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
            formulario = Hardware (tipo_hardware=data ['tipo'], marca_hardware = data ['marca'], stock_hardware= data ['stock'])
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
            formulario = Software (tipo_software=data ['tipo'], marca_software= data ['marca'], stock_software= data ['stock'])
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
            formulario = Insumos (tipo_insumo=data ['tipo'], marca_insumo= data ['marca'], stock_insumo= data ['stock'])
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
            formulario = Insumos (tipo_insumo=data ['tipo'], marca_insumo= data ['marca'], stock_insumo= data ['stock'])
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
            formulario = Software (tipo_software=data ['tipo'], marca_software= data ['marca'], stock_software= data ['stock'])
            formulario.save()
            return redirect ("agregado")
    else:
            mi_formulario = Formulario_software ()
    return render (request, "formulario_software.html", {'mi_formulario': mi_formulario})

def buscar_modelo_cel(request):
        if request.GET['modelo_cel']:
            modelo_buscado=request.GET['modelo_cel']
            celulares=Celulares.objects.filter(modelo_celular__icontains=modelo_buscado)
        
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
    



