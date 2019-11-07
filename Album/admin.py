from django.contrib import admin

# Register your models here.
from .models import Figuras

@admin.register(Figuras)
class EntradaAdmin(admin.ModelAdmin):
	list_display=['id_figura','nom_fugura','num_figura']