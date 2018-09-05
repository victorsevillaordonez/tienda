from django.urls import path
from .views import *


urlpatterns = [
	path('quienes_somos.html',quienes_somos_view),
	path('lista_productos.html',lista_productos_view,name='lista_productos_view'),
	path('agregar_producto.html',agregar_producto_view,name='agregar_producto_view'),
	path('ver_producto.html/<int:id_prod>/',ver_producto_view,name='ver_producto_view'),
	path('editar_producto.html/<int:id_prod>/',editar_producto_view,name='editar_producto_view'),
	path('eliminar_producto.html/<int:id_prod>/',eliminar_producto_view,name='eliminar_producto_view'),
	path('login.html',login_view,name='login_view'),
	path('logout.html', logout_view,name='logout_view'),
	path('registro_usuario.html', registrar_usuario_view,name='registrar_usuario_view'),
	path('ws/productos/', ws_productos_view,name='ws_productos_view'),
]