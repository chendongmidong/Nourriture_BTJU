from django.contrib import admin
from nourriture.models import Ingredient, Recipe, Recipe_Ingredient

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)
