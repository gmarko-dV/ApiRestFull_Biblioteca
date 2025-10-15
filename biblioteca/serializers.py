from rest_framework import serializers
from .models import Autor,Categoria,Libro

#Se crean los serializadores para convertir los datos a formato JSON.
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__' 

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' 

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__' 
                                