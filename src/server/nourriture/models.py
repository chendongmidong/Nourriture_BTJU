from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=254, null=True)
    price = models.IntegerField(null=True)
    heat = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    vitamin = models.FloatField()
    #Photo

    def __str__(self):
        return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(max_length=254, null=True)
	preparationTime = models.IntegerField()
	backingTime = models.IntegerField()
	howmanypeoples = models.IntegerField(null=True)
	ingredients = models.ManyToManyField(Ingredient, through='Recipe_Ingredient')
	count_view = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Religious(models.Model):
	name = models.CharField(max_length=42, unique=True)
	description = models.TextField(null=True)

class Recipe_Ingredient(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	recipe = models.ForeignKey(Recipe)
	quantity = models.IntegerField()

	## Enum pour différentes mesures
	#  Une pincée de sel
	#  500g de farine
	#  2 oeufs

	#Vidéo
	#Photo
	#Instructions
