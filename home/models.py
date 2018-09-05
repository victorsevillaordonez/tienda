from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Marca(models.Model):
	nombre = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length = 100)
	precio = models.IntegerField()
	stock = models.IntegerField()
	status = models.BooleanField(default=True)
	foto = models.ImageField(upload_to = 'fotos', null = True, blank = True)
	marca = models.ForeignKey(Marca,on_delete=models.PROTECT)
	def __str__(self):
		return self.nombre

class CategoriaProducto(models.Model):
	nombre = models.CharField(max_length = 100)
	categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
	producto = models.ForeignKey(Producto,on_delete=models.PROTECT)
	def __str__(self):
		return self.nombre

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	foto = models.ImageField(upload_to='profiles',null = True,blank=True)
	nombre = models.CharField(max_length=100)
