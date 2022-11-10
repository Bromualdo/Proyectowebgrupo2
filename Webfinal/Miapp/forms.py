from django import forms
from .models import Celulares,Insumos,Software,Hardware

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
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Motorola'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Moto G-82'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }

class Formulario_hardware (forms.ModelForm):
    class Meta:
        model=Hardware
        fields=('__all__')
        widgets={
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Motorola'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Moto G-82'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }

class Formulario_software (forms.ModelForm):
    class Meta:
        model=Software
        fields=('__all__')
        widgets={
            'tipo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Motorola'}),
            'marca':forms.TextInput(attrs={'class':'form-control','placeholder':'Ej:Moto G-82'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Cantidad'})
        }