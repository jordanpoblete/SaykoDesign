from django.urls import path
from .views import ilustracionApi, ilustracionpost
from .viewsLogin import login


urlpatterns = [
    path('ilustracion-api/<pk>', ilustracionApi, name='ilustracionApi'),
    path('ilustracion-api/', ilustracionpost, name= 'ilustracionpost'),
    path('login/', login, name='login'),
]