from rest_framework import viewsets
from .models import Autor,Categoria,Libro
from .serializers import AutorSerializer,CategoriaSerializer,LibroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer        

@api_view(['GET'])
def welcome(request):
    return Response({"message":"Bienvenido a la API de la Biblioteca"})    