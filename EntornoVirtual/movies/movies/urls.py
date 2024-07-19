"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf import settings
from pelicula import views as pelicula_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pelicula_views.index, name="home"),
    path('registrarse',core_views.registrarse, name="registrarse"),
    path('login',core_views.login, name="login"),
    path('',pelicula_views.detalle, name="detalle"),
]
