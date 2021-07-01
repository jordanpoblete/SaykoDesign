from rest_framework import serializers
from core.models import IlustracionIlu

class IlustracionIluSerializer(serializers.ModelSerializer):
    class Meta:
        model = IlustracionIlu
        fields = ['idIlustracion', 'nombre', 'descripcionIlu', 'fecha','categoria', 'imagen']