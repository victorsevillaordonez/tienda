from django.shortcuts import render
from .models import *
from .forms import agregar_producto_form, login_form, registro_usuario
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def quienes_somos_view(request):
	return render(request,'quienes_somos.html')

def lista_productos_view(request):
	if request.user.is_superuser:
		lista = Producto.objects.filter()
		return render(request,'lista_productos.html',locals())
	else:
		return redirect('/')
"""CRUD PARA PRODUCTO"""
def agregar_producto_view(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST,request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_productos.html')
	else:
		formulario = agregar_producto_form()
	return render(request,'agregar_producto.html',locals())

def ver_producto_view(request,id_prod):
	p = Producto.objects.get(id=id_prod)
	return render(request,'ver_producto.html',locals())

def editar_producto_view(request,id_prod):
	p = Producto.objects.get(id=id_prod)
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST,request.FILES, instance=p)
		if formulario.is_valid():
			p = formulario.save()
			return redirect ('/lista_productos.html')
	else:
		formulario = agregar_producto_form(instance=p)
	return render(request,'agregar_producto.html',locals())

def eliminar_producto_view(request,id_prod):
	prod = Producto.objects.get(id=id_prod)
	prod.delete()
	return redirect ('/lista_productos.html')
"""FIN CRUD"""

"""AUTENTICACION"""
def login_view(request):
	usu = ""
	cla = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return redirect('agregar_producto.html')
			else:
				msj = "Usuario o clave incorrecta"
		formulario = login_form()
	return render(request,'login.html',locals())

def logout_view(request):
	logout(request)
	return redirect('login.html')

def registrar_usuario_view(request):
	formulario = registro_usuario()
	if request.method == 'POST':
		formulario = registro_usuario(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['usuario']
			email = formulario.cleaned_data['email']
			password = formulario.cleaned_data['password1']
			confirmarPassword = formulario.cleaned_data['password2']
			u = User.objects.create_user(username=usuario,email=email,password=password)
			u.save()
			return render(request,'Bienvenido.html',locals())
		else:
			return render(request,'registro_usuario.html',locals())
	return render(request,'registro_usuario.html',locals())

"""Implementación de webservices"""
def ws_productos_view(request):
	data = serializers.serialize('json',Producto.objects.filter(status = True))
	return HttpResponse(data,content_type='application/json')
