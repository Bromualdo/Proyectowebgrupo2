from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Celulares, Insumos,Hardware,Software
from .forms import UserRegisterForm,Formulario_Insumos, Formulario_celulares, Formulario_hardware, Formulario_software
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
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

def show_cel_del(request):
    lista=Celulares.objects.all()
    return render(request,"show_cel_del.html",{"Celulares":lista})

def show_cel_edit(request):
    lista=Celulares.objects.all()
    return render(request,"show_cel_edit.html",{"Celulares":lista})
    

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

def login_usuario (request):

    if request.method == 'POST':

        formulario_login_usuario = AuthenticationForm(request, data=request.POST)

        if formulario_login_usuario.is_valid():

            data = formulario_login_usuario.cleaned_data

            nombre_usuario = data["username"]
            password_usuario = data["password"]

            user = authenticate(username=nombre_usuario, password=password_usuario)

            if user:

                login(request, user)

                return render(request, "inicio2.html", {"mensaje": f'Bienvenido {nombre_usuario}'})
            
            else:

                return render(request, "inicio2.html", {"mensaje": f'Error, datos incorrectos'})

        return render(request, "inicio2.html", {"mensaje": f'Error, formulario invalido'})

    else:

        formulario_login_usuario = AuthenticationForm()

        return render(request, "login.html", {"formulario_login": formulario_login_usuario})


def eliminar_celular(request,id):
    
    if request.method == "POST":
        
        celulares= Celulares.objects.get(id=id)
        celulares.delete()        
        # celulares=Celulares.objects.all()
        
        return render(request, "show_cel_del_exito.html", {'celulares': celulares})    

def editar_celular(request,id):
    
    celulares=Celulares.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_celulares (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            
            celulares.marca=data["marca"]
            celulares.modelo=data["modelo"]
            celulares.stock=data["stock"]            
            celulares.save()
            return redirect("show_cel_edit")
    else:
            mi_formulario = Formulario_celulares(initial={
                "marca": celulares.marca,
                "modelo": celulares.modelo,
                "stock": celulares.stock
            })
    return render (request, "show_cel_edit_menu.html", {'mi_formulario': mi_formulario,"id":celulares.id})    

 



