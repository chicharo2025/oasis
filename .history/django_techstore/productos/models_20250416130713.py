from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
   

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.FloatField()
    destacado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos/')
    en_oferta = models.BooleanField(default=False)
    detalle = models.TextField(default="Sin detalles")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    




