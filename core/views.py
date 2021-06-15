from django.shortcuts import render
from django.shortcuts import redirect
from .models import Peticion, IlustracionIlu
from .forms import PeticionForm, IlustracionIluForm

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










def ilustracionesIlu(request):
   ilustracionesIlu = IlustracionIlu.objects.all()
   datos = {
      'ilustracionesIlu': ilustracionesIlu
   }
   return render(request, 'core/lista-Ilustraciones.html', datos)


def add_ilustraciones(request):
    datos = {'form': IlustracionIluForm()}
    if request.method == 'POST':
        formulario = IlustracionIluForm(request.POST, request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'core/add-ilustraciones.html', datos)


def mod_ilustraciones(request, pk):
   ilustracionIlu = IlustracionIlu.objects.get(idIlustracion=pk)
   
   if request.method == 'POST':
      formulario_mod = IlustracionIluForm( request.POST, request.FILES, instance = ilustracionIlu)
      if formulario_mod.is_valid:
         formulario_mod.save()
      return redirect (to= "ilustracionesIlu")

   else:
         datos = {
            'form': IlustracionIluForm(instance=ilustracionIlu)
         }
         return render(request, 'core/mod-ilustraciones.html',datos)


def delete_ilustraciones(request, pk):
   ilustracionIlu = IlustracionIlu.objects.get(idIlustracion=pk)
   ilustracionIlu.delete()
   return redirect(to="ilustracionesIlu")




