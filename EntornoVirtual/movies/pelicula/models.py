from django.db import models

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=200)
    descripcion = models.TextField(verbose_name="Descripción",default='no disponible')
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de lanzamiento",default='no disponible')
    duracion = models.IntegerField(verbose_name="Duración",help_text="Duración en minutos")
    imagen = models.ImageField(verbose_name="Imagen",upload_to="pelicula"),
    director = models.TextField(verbose_name="Director",default='no disponible')
    genero = models.CharField(max_length=100,verbose_name="Género",default='no disponible')
    
    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"