from django import forms
from .models import Figuras

class FigurasForm(forms.Form):
	nom_fugura= forms.CharField(label= 'Nombres:',max_length= 80)
	num_figura= forms.CharField(label= 'Numero:',max_length= 80)