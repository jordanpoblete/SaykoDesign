from django.urls import path
from api_pumba.views import ilustracionApi

urlpatterns = [
    path('ilustracion-api/', ilustracionApi, name='ilustracionApi'),
]