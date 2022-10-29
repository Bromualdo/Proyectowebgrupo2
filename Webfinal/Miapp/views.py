from http.client import HTTPResponse
from django.shortcuts import render
from django.template import Context, Template
from .models import Celulares,Insumos,Hardware,Software

# Create your views here.

def inicio (request):
    return render(request,"inicio.html")
    
def celulares (request):
    return render(request, "lista_celulares.html")

def hardware (request):
    return render(request, "lista_hardware.html")

def software (request):
    return render(request, "lista_software.html")

def insumos (request):
    return render (request, "lista_insumos.html")

 