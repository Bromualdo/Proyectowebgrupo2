from django import forms
from .models import Celulares,Insumos,Software,Hardware
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group


class Formulario_celulares (forms.ModelForm):
    class Meta:
        model=Celulares
        fields=('__all__')
        widgets={
            'marca': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Motorola'}),
            'modelo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Moto G-82'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }

class Formulario_Insumos (forms.ModelForm):
    class Meta:
        model=Insumos
        fields=('__all__')
        widgets={
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:DVD RW'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Sony'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }

class Formulario_hardware (forms.ModelForm):
    class Meta:
        model=Hardware
        fields=('__all__')
        widgets={
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Impresora'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej: HP-2491'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }

class Formulario_software (forms.ModelForm):
    class Meta:
        model=Software
        fields=('__all__')
        widgets={
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Windowss 11'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Microsoft'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }


class UserRegisterForm (UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Ingrese nombre de usuario', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'Ingrese correo electrónico', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Ingrese contraseña', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Repita contraseña', 
            'maxlength':'22',  
            'minlength':'8' 
            })
        self.fields['group'].widget.attrs.update({
            'class': 'custom-select',
            'id':"choose"
            
        })
        
        
  
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100)
    group=forms.ModelChoiceField(queryset=Group.objects.all(),required=True) 
    

    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2','group') 

