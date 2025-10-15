from rest_framework import serializers
from .models import Autor,Categoria,Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        field = ['id','nombre','bibliografia','fecha_nacimiento']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        field = ['id','nombre']

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        field = ['id','titulo','descripcion','autor','categoria','fecha_publi','isbn']
                                