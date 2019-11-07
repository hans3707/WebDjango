"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog import views as Vistas
from Album import views as Album
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', Vistas.welcome,name='bienvenida'),
    path('entradas/',Vistas.entradas,name='entradas'),
    path('autores/', Vistas.autores,name='autores'),
    path('',Vistas.index,name='inicio'),
    path('Album/',Album.album,name='album'),
    path('registro/',Album.registro,name='registro'),
    path('faltantes/', Album.faltantes,name='faltantes'),
]