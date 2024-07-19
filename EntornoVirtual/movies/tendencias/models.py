from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="imagen")
    datos = models.TextField()
    director = models.TextField()
    director2 = models.TextField()   
    escritor = models.TextField()

    
    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"
