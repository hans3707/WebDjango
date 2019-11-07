from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Autor
from .models import Entrada

from.forms import *

def welcome(request):
	#nombres = Autor.objects.all()
	return render(request,'welcome.html')
	#return render(request,'welcome.html',{'nombre':nombres})
	#return HttpResponse(f'<h1>algo</h1> {nombre}')
def autores(request):
	if request.method == 'POST':
		form = AutorForm(request.POST)
		if form.is_valid():
			autor = Autor()
			autor.nombres = form.cleaned_data['nombres']
			autor.apellidos = form.cleaned_data['apellidos']
			autor.save()
			return redirect('autores')
	else:
		form= AutorForm
		todosAutores= Autor.objects.all()
		return render(request,'autores.html',{'autores':todosAutores, 'form':form})

def entradas(request):
	form2= EntradaForm
	todasEntradas= Entrada.objects.all()
	return render(request,'entradas.html',{'entradas':todasEntradas,'form2':form2})

def index(request):
	return HttpResponse('<h1>Index</h1><a href="welcome">Bienvenido')

