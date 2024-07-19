from django.shortcuts import render, get_object_or_404
from .models import tendencias
from django.http import JsonResponse
# Create your views here.
def index(request):
    publicaciones = tendencias.objects.all()
    return render(request,"tendencias/index.html",{'publicaciones':publicaciones})

    
#def detalle(request):
#    return render(request,"core/detalle.html") 
def detalle(request, id):
    publicacion = get_object_or_404(tendencias, id=id)
    return render(request, 'tendencias/detalle.html', {'publicacion': publicacion})

