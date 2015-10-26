from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=254, null=True)
    price = models.IntegerField(null=True)
    heat = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbohydrate = models.FloatField(null=True)
    vitamin = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(max_length=254, null=True)
	preparationTime = models.IntegerField(null=True)
	backingTime = models.IntegerField(null=True)
	howmanypeoples = models.IntegerField(null=True)
	ingredients = models.ManyToManyField(Ingredient, through='Recipe_Ingredient')
	count_view = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Religion(models.Model):
	name = models.CharField(max_length=42, unique=True)
	description = models.TextField(null=True)
	forbidden_ingredients = models.ManyToManyField(Ingredient)

class Intolerence(models.Model):
	name = models.CharField(max_length=42, unique=True)
	description = models.TextField(null=True)
	forbidden_ingredients = models.ManyToManyField(Ingredient)

class Alergie(models.Model):
	name = models.CharField(max_length=42, unique=True)
	description = models.TextField(null=True)
	forbidden_ingredients = models.ManyToManyField(Ingredient)

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
