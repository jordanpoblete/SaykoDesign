from django.shortcuts import render
from .serializers import IlustracionIluSerializer
from core.models import IlustracionIlu
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def ilustracionpost(request):
        """
        Lista todos las Ilustraciones
        """
        if request.method == 'GET':
            ilustraciones_lista = IlustracionIlu.objects.all()
            serializer = IlustracionIluSerializer(ilustraciones_lista, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
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

@api_view(['GET', 'PUT', 'DELETE'])
def ilustracionApi(request, pk):
    try:
        ilustracionesIlu = IlustracionIlu.objects.get(idIlustracion = pk)
    except IlustracionIlu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    GET: Mostrar ilustracion singular singular singular singular segun primary key
    """
    if request.method == 'GET':
        serializer = IlustracionIluSerializer(ilustracionesIlu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        """
        PUT: Editar un vehiculo por patente
        """
        data = JSONParser().parse(request)
        serializer = IlustracionIluSerializer(ilustracionesIlu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        """
        Elimina una ilustracion
        """
        ilustracionesIlu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")
    
    #Validamos el password
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta")

    #permite crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    # devolvemos el token
    return Response(token.key)