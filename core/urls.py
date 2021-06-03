from django.urls import path
from .views import index, ilustraciones

urlpatterns = [
    path('index/', index, name="index"),
    path('ilustraciones/', ilustraciones, name="ilustraciones"),
]
