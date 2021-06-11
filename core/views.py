from django.shortcuts import render
from django.shortcuts import redirect
from .models import Peticion
from .forms import PeticionForm

# Create your views here.
def index(request):
   return render(request, 'core/index.html')

def descripcion(request):
   return render(request, 'core/descripcion_ilustracion1.html')

def disenhos(request):
   return render(request, 'core/disenhos.html')

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


def add_peticiones(request):
    datos = {'form': PeticionForm()}
    if request.method == 'POST':
        formulario = PeticionForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'core/add_peticiones.html', datos)


def mod_peticiones(request, pk):
   peticion = Peticion.objects.get(idPeticion=pk)
   datos = {
      'form' : PeticionForm(instance=peticion)
   }
   if request.method == 'POST':
      formulario_mod = PeticionForm(data= request.POST, instance = peticion)
      if formulario_mod.is_valid:
         formulario_mod.save()
         datos['mensaje'] = "Modificado"
   return render (request, 'core/mod_peticiones.html', datos)


def delete_peticiones(request, pk):
   peticion = Peticion.objects.get(idPeticion=pk)
   peticion.delete()
   return redirect(to="peticiones")




