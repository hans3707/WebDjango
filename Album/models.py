from django.db import models

# Create your models here.

class Figuras(models.Model):
	id_figura = models.AutoField(primary_key = True)
	nom_fugura = models.CharField(max_length = 120)
	num_figura = models.IntegerField(default=0)

	