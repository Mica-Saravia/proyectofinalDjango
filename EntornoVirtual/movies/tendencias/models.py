from django.db import models

# Create your models here.

class tendencias(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="publicacion")
    datos = models.TextField()
    director = models.TextField()
    director2 = models.TextField()   
    escritor = models.TextField()
