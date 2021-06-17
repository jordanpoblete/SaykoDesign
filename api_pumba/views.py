from django.shortcuts import render
from .serializers import IlustracionIluSerializer
from core.models import IlustracionIlu
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def ilustracionApi(request):
    """
    Lista todos las Ilustraciones
    """
    if request.method == 'GET':
        ilustraciones_lista = IlustracionIlu.objects.all()
        serializer = IlustracionIluSerializer(ilustraciones_lista, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Agrega una Ilustracion
        """
        data = JSONParser().parse(request)
        serializer = IlustracionIluSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
