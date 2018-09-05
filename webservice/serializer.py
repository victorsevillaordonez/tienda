from rest_framework import serializers
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('url','nombre','status','foto','precio','stock','marca',)


class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('nombre',)


class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url','nombre',)