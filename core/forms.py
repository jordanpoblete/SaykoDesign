from django import forms
from django.forms import ModelForm
from .models import Peticion



class PeticionForm(ModelForm):

    class Meta:
        model = Peticion
        fields = ['idPeticion','correo','descripcion','categoria']