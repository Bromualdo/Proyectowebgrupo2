from django import forms

class Formulario_Insumos (forms.Form):
    tipo= forms.CharField ()
    marca= forms.CharField ()
    stock= forms.IntegerField ()

class Formulario_hardware (forms.Form):
    tipo= forms.CharField ()
    marca= forms.CharField ()
    stock= forms.IntegerField()

class Formulario_software (forms.Form):
    tipo= forms.CharField () 
    marca= forms.CharField ()
    stock= forms.IntegerField()

class Formulario_celulares (forms.Form):
    marca= forms.CharField ()
    modelo= forms.CharField ()
    stock= forms.IntegerField ()


