from django import forms
from .models import Celulares,Insumos,Software,Hardware
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


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
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Microsof'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')