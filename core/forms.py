from django import forms
from django.forms import ModelForm
from .models import Peticion, IlustracionIlu



class PeticionForm(ModelForm):

    class Meta:
        model = Peticion
        fields = ['idPeticion','correo','descripcion','categoria']



class IlustracionIluForm(ModelForm):

    class Meta:
        model = IlustracionIlu
        fields = ['idIlustracion','nombre','descripcionIlu','fecha','categoria','imagen']