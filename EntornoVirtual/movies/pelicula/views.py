from django.shortcuts import render, get_object_or_404
from .models import Pelicula
from django.http import JsonResponse
# Create your views here.
def index(request):
    publicaciones = Pelicula.objects.all()
    return render(request,"pelicula/index.html",{'publicaciones':publicaciones})

    
#def detalle(request):
#    return render(request,"core/detalle.html") 
def detalle(request, id):
    publicacion = get_object_or_404(Pelicula, id=id)
    return render(request, 'pelicula/detalle.html', {'publicacion': publicacion})

