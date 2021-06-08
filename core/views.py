from django.shortcuts import render
from .models import Peticion
from .forms import PeticionForm

# Create your views here.
def index(request):
   return render(request, 'core/index.html')

def descripcion(request):
   return render(request, 'core/descripcion_ilustracion1.html')

def diseños(request):
   return render(request, 'core/diseños.html')

def formulario(request):
   return render(request, 'core/formulario.html')

def graffitis(request):
   return render(request, 'core/graffitis.html')

def geolocalizacion(request):
   return render(request, 'core/Geolocalizacion.html')

def identidades(request):
   return render(request, 'core/Identidades.html')

def ilustraciones(request):
   return render(request, 'core/ilustraciones.html')

def login(request):
   return render(request, 'core/login.html')

def portadas(request):
   return render(request, 'core/portadas.html')

def recuperarcontra(request):
   return render(request, 'core/recuperarcontra.html')

def register(request):
   return render(request, 'core/registrar.html')

def api1(request):
   return render(request, 'core/uso_api.html')



# Base de datos

def peticiones(request):
   peticiones = Peticion.objects.all()
   datos = {
      'peticiones': peticiones
   }
   return render(request, 'core/peticiones.html', datos)


def add_peticion(request):
    datos = {'form': PeticionForm()}
    if request.method == 'POST':
        formulario = PeticionForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'core/add_peticion.html', datos)
