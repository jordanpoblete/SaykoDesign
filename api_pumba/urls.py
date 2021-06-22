from django.urls import path
from api_pumba.views import ilustracionApi, ilustracionpost

urlpatterns = [
    path('ilustracion-api/<pk>', ilustracionApi, name='ilustracionApi'),
    path('ilustracion-api/', ilustracionpost, name= 'ilustracionpost')
]