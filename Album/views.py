from django.shortcuts import render
from django.shortcuts import redirect
from .models import Figuras

from.forms import *

# Create your views here.
def album(request):
	return render(request,'index.html',{'range':range(700)})

def registro(request):
	if request.method == 'POST':
		form = FigurasForm(request.POST)
		if form.is_valid():
			figuras = Figuras()
			figuras.nom_fugura = form.cleaned_data['nom_fugura']
			figuras.num_figura = form.cleaned_data['num_figura']
			figuras.save()
			return redirect('registro')
	else:
		form= FigurasForm
		todosFiguras= Figuras.objects.all()
		return render(request,'registro.html',{'figuras':todosFiguras, 'form':form,'range':range(700)})

def faltantes(request):
	return render(request,'faltantes.html')