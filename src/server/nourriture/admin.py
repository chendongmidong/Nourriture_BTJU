from django.contrib import admin
from nourriture.models import Ingredient, Recipe, Recipe_Ingredient, Religion, Intolerence, Alergie

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)
admin.site.register(Religion)
admin.site.register(Intolerence)
admin.site.register(Alergie)
