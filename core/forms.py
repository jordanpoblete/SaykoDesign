from django import forms
from django.forms import ModelForm
from .models import Peticion



class UsuarioForm(ModelForm):

    class Meta:
        model = Peticion
        fields = ['idUsuario','correo','descripcion','categoria']