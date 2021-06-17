from django.urls import path
from api_pumba.views import ilustracionIlu

urlpatterns = [
    path('ilustracion-api/', ilustracionIlu, name='ilustracionesIlu'),
]