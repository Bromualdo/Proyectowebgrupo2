from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Celulares, Insumos,Hardware,Software
from .forms import UserRegisterForm,Formulario_Insumos, Formulario_celulares, Formulario_hardware, Formulario_software, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.models import User,Group
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.




def inicio (request):
    return render(request,"inicio.html")


@login_required
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
    
@permission_required('Miapp.add_hardware', raise_exception=True)
@login_required   
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

@permission_required('Miapp.add_software', raise_exception=True)
@login_required  
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
 
@permission_required('Miapp.add_insumos', raise_exception=True)    
@login_required  
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
    
@permission_required('Miapp.delete_celulares', raise_exception=True)   
@login_required(login_url='Inicio')  
def agregado (request):
    return render (request, "agregado.html")


@permission_required('Miapp.add_insumo', raise_exception=True)      
@login_required(login_url='Inicio')  
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


@permission_required('Miapp.add_software', raise_exception=True)        
@login_required(login_url='Inicio')  
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


@permission_required('Miapp.change_celulares', raise_exception=True)         
@login_required(login_url='Inicio')  
def buscar_modelo_cel(request):
        if request.GET['busqueda']:
            modelo_buscado=request.GET['busqueda']
            celulares=Celulares.objects.filter(modelo__icontains=modelo_buscado)
            print(celulares)
        
            return render(request,"busqueda_cel.html",{"celulares":celulares,"modelo":modelo_buscado,})
        else:
            respuesta="usted ha ingresado datos en blanco, intente de nuevo"
        return render(request,'busqueda_cel.html',{"respuesta":respuesta})
    

@permission_required('Miapp.view_celulares', raise_exception=True)        
@login_required(login_url='Inicio')  
def show_celulares(request):
    lista = Celulares.objects.all()    
    return render(request, "show_cel.html",{"Celulares": lista} )

@permission_required('Miapp.view_insumos', raise_exception=True)      
@login_required(login_url='Inicio')  
def show_insumos(request):
    lista = Insumos.objects.all()    
    return render(request, "show_insumos.html",{"Insumos": lista} )

@permission_required('Miapp.view_software', raise_exception=True)      
@login_required(login_url='Inicio')  
def show_soft(request):
    lista = Software.objects.all()    
    return render(request, "show_soft.html",{"Software": lista} )

@permission_required('Miapp.view_hardware', raise_exception=True)      
@login_required(login_url='Inicio')  
def show_hard(request):
    lista = Hardware.objects.all()    
    return render(request, "show_hard.html",{"Hardware": lista} )

@permission_required('Miapp.delete_celulaares', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_cel_del(request):
    lista=Celulares.objects.all()
    return render(request,"show_cel_del.html",{"Celulares":lista})

@permission_required('Miapp.delete_celulares', raise_exception=True)   
@login_required(login_url='Inicio')  
def usuarios(request):
    all_user=User.objects.values()              
    
    # asig=usuario.groups.add(3,1)# siendo 3 usuario y 1 el grupo
    
    
    return render(request,"gestion_de_usuarios.html",{'Usuarios':all_user})

@permission_required('Miapp.change_celulares', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_cel_edit(request):
    lista=Celulares.objects.all()
    return render(request,"show_cel_edit.html",{"Celulares":lista})

@permission_required('Miapp.delete_hardware', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_hard_del(request):
    lista=Hardware.objects.all()
    return render(request,"show_hard_del.html",{"Hardware":lista})

@permission_required('Miapp.change_hardware', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_hard_edit(request):
    lista=Hardware.objects.all()
    return render(request,"show_hard_edit.html",{"Hardware":lista})

@permission_required('Miapp.delete_insumos', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_ins_del(request):
    lista=Insumos.objects.all()
    return render(request,"show_ins_del.html",{"Insumos":lista})

@permission_required('Miapp.change_insumos', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_ins_edit(request):
    lista=Insumos.objects.all()
    return render(request,"show_ins_edit.html",{"Insumos":lista})

@permission_required('Miapp.delete_software', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_soft_del(request):
    lista=Software.objects.all()
    return render(request,"show_soft_del.html",{"Software":lista})

@permission_required('Miapp.change_software', raise_exception=True)   
@login_required(login_url='Inicio')  
def show_soft_edit(request):
    lista=Software.objects.all()
    return render(request,"show_soft_edit.html",{"Software":lista})

@permission_required('Miapp.delete_celulares', raise_exception=True)   
@login_required(login_url='Inicio') 
def registro_usuario (request):
    if request.method == 'POST':
    
        formulario_registro_usuario = UserRegisterForm(request.POST)

        
        if formulario_registro_usuario.is_valid():
	
            nombre_usuario=formulario_registro_usuario.cleaned_data["username"] 
            nombre_grupo=formulario_registro_usuario.cleaned_data["group"] 
            formulario_registro_usuario.save()
            
            nuevo_usuario=User.objects.get(username=nombre_usuario)
            
            asigno_grupo=Group.objects.get(name=nombre_grupo)
                              
            nuevo_usuario.groups.add(asigno_grupo.id)                   
                                           
            	        
            return render(request, "inicio2.html", {"mensaje": f'El usuario {nombre_usuario} ha sido creado con éxito bajo el grupo {nombre_grupo}'})
	    
        else:
	    
            return render(request, "inicio2.html", {"mensaje": f'Error al crear usuario'})
    else:
        formulario_registro_usuario = UserRegisterForm()
	    
        return render(request, "formulario_registro_usuario.html", {"form": formulario_registro_usuario})

   

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


@permission_required('Miapp.delete_celulares', raise_exception=True)   
@login_required(login_url='Inicio')  
def eliminar_celular(request,id):
    
    if request.method == "POST":
        
        celulares= Celulares.objects.get(id=id)
        celulares.delete()        
       
        
        return render(request, "show_cel_del_exito.html", {'celulares': celulares})    

@permission_required('Miapp.change_celulares', raise_exception=True)
@login_required(login_url='Inicio')  
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

@permission_required('Miapp.delete_hardware', raise_exception=True)
@login_required(login_url='Inicio')  
def eliminar_hardware(request,id):
    
    if request.method == "POST":
        
        Hard= Hardware.objects.get(id=id)
        Hard.delete()        
        
        
        return render(request, "show_hard_del_exito.html", {'Hardware': Hard})    

@permission_required('Miapp.change_hardware', raise_exception=True)
@login_required(login_url='Inicio')  
def editar_hardware(request,id):
    
    Hard=Hardware.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_hardware (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            
            
            Hard.tipo=data["tipo"]
            Hard.marca=data["marca"]
            Hard.stock=data["stock"]            
            Hard.save()
            return redirect("show_hard_edit")
    else:
            mi_formulario = Formulario_hardware(initial={
                "tipo": Hard.tipo,
                "marca": Hard.marca,
                "stock": Hard.stock
            })
    return render (request, "show_hard_edit_menu.html", {'mi_formulario': mi_formulario,"id":Hard.id})

@permission_required('Miapp.delete_insumos', raise_exception=True)
@login_required(login_url='Inicio')  
def eliminar_insumos(request,id):
    
    if request.method == "POST":
        
        Ins= Insumos.objects.get(id=id)
        Ins.delete()        
        
        
        return render(request, "show_ins_del_exito.html", {'Insumos': Ins})    

@permission_required('Miapp.change_insumos', raise_exception=True)
@login_required(login_url='Inicio')  
def editar_insumos(request,id):
    
    Ins=Insumos.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_Insumos (request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            
            
            Ins.tipo=data["tipo"]
            Ins.marca=data["marca"]
            Ins.stock=data["stock"]            
            Ins.save()
            return redirect("show_ins_edit")
    else:
            mi_formulario = Formulario_hardware(initial={
                "tipo": Ins.tipo,
                "marca": Ins.marca,
                "stock": Ins.stock
            })
    return render (request, "show_ins_edit_menu.html", {'mi_formulario': mi_formulario,"id":Ins.id})

@permission_required('Miapp.delete_software', raise_exception=True)
@login_required(login_url='Inicio')  
def eliminar_software(request,id):
    
    if request.method == "POST":
        
        Soft= Software.objects.get(id=id)
        Soft.delete()        
        
        
        return render(request, "show_soft_del_exito.html", {'Software': Soft})    
    

@permission_required('Miapp.change_software', raise_exception=True)
@login_required(login_url='Inicio')  
def editar_software(request,id):
    
    Soft=Software.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Formulario_software(request.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            
            
            Soft.tipo=data["tipo"]
            Soft.marca=data["marca"]
            Soft.stock=data["stock"]            
            Soft.save()
            return redirect("show_soft_edit")
    else:
            mi_formulario = Formulario_software(initial={
                "tipo": Soft.tipo,
                "marca": Soft.marca,
                "stock": Soft.stock
            })
    return render (request, "show_soft_edit_menu.html", {'mi_formulario': mi_formulario,"id":Soft.id}) 
