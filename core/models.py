from django.db import models

# Create your models here.


#Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la Categoría")

    def __str__(self):
        return self.nombreCategoria

#Modelo para usuarios
class Usuario(models.Model):
    idUsuario= models.IntegerField(primary_key=True, verbose_name='Id de Usuario')
    correo= models.CharField(max_length=60,  verbose_name="correo")
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.correo