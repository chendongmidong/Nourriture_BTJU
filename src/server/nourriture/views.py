from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

from django.core import serializers

import json

from nourriture.models import Ingredient, Recipe, Recipe_Ingredient

def home(request):
	"""Home page"""
	return render(request, 'nourriture/home.html', locals())

def ingredientView(request):
	response = serializers.serialize("json", Ingredient.objects.all())

	return HttpResponse(response)

@csrf_exempt
def ingredientAdd(request):
	if request.method != 'POST':
		return sendError('No post request')

	if request.POST['name'] is None:
		return sendError('Name not defined')

	if len(Ingredient.objects.filter(name=request.POST["name"])) != 0:
		return sendError('Name already used')

	newIngredient = Ingredient(name=request.POST.get('name', "None"),
							   description=request.POST.get('description', None),
							   price=request.POST.get('price', None))

	newIngredient.save()

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success', 'id': newIngredient.id}))

@csrf_exempt
def ingredientDelete(request):
	if request.method != 'POST':
		return sendError('No post request')

	if request.POST['id'] is None:
		return sendError('Id not defined')

	ingredient = Ingredient.objects.get(id=request.POST['id'])

	if ingredient:
		ingredient.delete()
	else:
		return sendError('Id not found')

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success'}))

@csrf_exempt
def ingredientUpdate(request):
	if request.method != 'POST':
		return sendError('No post request')

	if request.POST['name'] is None:
		return sendError('Name not defined')

	if request.POST['id'] is None:
		return sendError('Id not defined')

	ingredient = Ingredient.objects.get(id=request.POST['id'])

	if ingredient is None:
		return sendError()

	ingredient.name = request.POST.get('name', "None")
	ingredient.description = request.POST.get('description', None)
	ingredient.price = request.POST.get('price', None)

	ingredient.save()

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success', 'id': ingredient.id}))

@csrf_exempt
def recipeAdd(request):
	if request.method != 'POST':
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error', 'error': 'No post request'}))

	if request.POST['name'] is None:
		return sendError('Name not defined')

	recipeIngredients = request.POST.getlist('ingredients', None)

	ingredientSet = checkIngredient(recipeIngredients)

	if ingredientSet is False:
		return sendError('Ingredients error')

	newRecipe = Recipe(name=request.POST['name'],
					   description=request.POST.get('description', None))

	newRecipe.save()

	for ingredient in ingredientSet:
		Recipe_Ingredient.objects.create(ingredient=ingredient,
										 recipe=newRecipe,
										 quantity=1)

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success', 'id': newRecipe.id}))

# @csrf_exempt
# def recipeDelete

def checkIngredient(ingredients):
	if ingredients is None:
		return False
	ingredientSet = list()
	for ingredient in ingredients:
		ing = Ingredient.objects.get(id=ingredient)
		if ing is None:
			return False
		ingredientSet.append(ing)

	return ingredientSet

def sendError(error=None, status=400):
	if error is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}), status=status)
	else:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error', 'error': error}), status=status)


