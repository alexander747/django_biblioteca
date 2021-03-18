from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']

        labels = {
            'nombre':'Nombre del autor',
            'apellidos':'Apellidos del autor',
            'nacionalidad':'Nacionalidad',
            'descripcion':'Descripción'
        }


        widgets = {
             'nombre': forms.TextInput(
                 attrs = {
                     'class':'form-control',
                     'placeholder':'Ingrese nombre del autor',
                     'id':'nombre'
                 }
             ),
             'apellidos': forms.TextInput(
                 attrs = {
                     'class':'form-control',
                     'placeholder':'Ingrese apellidos',
                     'id':'apellidos'
                 }
             ),
             'nacionalidad': forms.TextInput(
                 attrs = {
                     'class':'form-control',
                     'placeholder':'Ingrese nacionalidad',
                     'id':'nacionalidad'
                 }
             ),
             'descripcion': forms.Textarea(
                 attrs = {
                     'class':'form-control',
                     'placeholder':'Descripción',
                     'id':'descripcion'
                 }
             )
        }