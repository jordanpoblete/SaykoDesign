from django.urls import path
from .views import index, descripcion, disenhos, formulario, graffitis, geolocalizacion, identidades, ilustraciones, login, portadas, recuperarcontra, register, api1, peticiones, add_peticiones, mod_peticiones, delete_peticiones, ilustracionesIlu, add_ilustraciones, mod_ilustraciones, delete_ilustraciones

urlpatterns = [
    path('index/', index, name="index"),
    path('descripcion/', descripcion, name="descripcion"),
    path('disenhos/', disenhos, name="disenhos"),
    path('formulario/', formulario, name="formulario"),
    path('graffitis/', graffitis, name="graffitis"),
    path('geolocalizacion/', geolocalizacion, name="geolocalizacion"),
    path('identidades/', identidades, name="identidades"),
    path('ilustraciones/', ilustraciones, name="ilustraciones"),
    path('login/', login, name="login"),
    path('portadas/', portadas, name="portadas"),
    path('recuperarcontra/', recuperarcontra, name="recuperarcontra"),
    path('register/', register, name="register"),
    path('api1/', api1, name="api1"),
    path('peticiones/', peticiones, name="peticiones"),
    path('add_peticiones/', add_peticiones, name="add_peticiones"),
    path('mod_peticiones/<pk>/', mod_peticiones, name="mod_peticiones"),
    path('delete_peticiones/<pk>/', delete_peticiones, name="delete_peticiones"),
    path('ilustracionesIlu/', ilustracionesIlu, name="ilustracionesIlu"),
    path('add_ilustraciones/', add_ilustraciones, name="add_ilustraciones"),
    path('mod_ilustraciones/<pk>/', mod_ilustraciones, name="mod_ilustraciones"),
    path('delete_ilustraciones/<pk>/', delete_ilustraciones, name="delete_ilustraciones"),
    
]
