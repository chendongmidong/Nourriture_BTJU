from nourriture.models import Ingredient, Recipe
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'price', 'heat', 'protein', 'fat', 'carbohydrate', 'vitamin')

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients')
