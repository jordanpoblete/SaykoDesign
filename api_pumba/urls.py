from django.urls import path
from .views import ilustracionApi, ilustracionpost
from .views import login


urlpatterns = [
    path('ilustracion-api/<pk>', ilustracionApi, name='ilustracionApi'),
    path('ilustracion-api/', ilustracionpost, name= 'ilustracionpost'),
    path('login/', login, name='login'),
]