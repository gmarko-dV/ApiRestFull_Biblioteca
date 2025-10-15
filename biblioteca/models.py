from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    bibliografia = models.TextField(blank = True)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=150)
    autor = models.ForeignKey(Autor,related_name='libros',on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,related_name='libros',on_delete=models.CASCADE)
    fecha_publi = models.DateField()
    isbn = models.CharField(max_length=13)
    
    
    def __str__(self):
        return self.titulo