
# Register your models here.+

from django.contrib import admin
from .models import Categoria, Peticion, IlustracionIlu

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Peticion)
admin.site.register(IlustracionIlu)