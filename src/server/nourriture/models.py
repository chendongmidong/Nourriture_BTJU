from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=254, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=254, null=True)
	ingredient = models.ManyToManyField(Ingredient, through='Recipe_Ingredient')

class Recipe_Ingredient(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	recipe = models.ForeignKey(Recipe)
	quantity = models.IntegerField()
	## Enum pour différentes mesures
	#  Une pincée de sel
	#  500g de farine
	#  2 oeufs
