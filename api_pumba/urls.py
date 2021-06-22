from django.urls import path
from api_pumba.views import ilustracionApis, ilustracionApi

urlpatterns = [
    path('ilustracion-api/', ilustracionApis, name='ilustracionApis'),
    path ('ilustracion-api/<pk>', ilustracionApi, name= "ilustracionApi")
]