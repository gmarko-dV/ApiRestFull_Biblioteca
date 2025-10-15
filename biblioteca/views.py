from rest_framework import viewsets
from .models import Autor,Categoria,Libro
from .serializers import AutorSerializer,CategoriaSerializer,LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.object.all()
    serializer_class = CategoriaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer        