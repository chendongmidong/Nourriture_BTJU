from nourriture.models import Ingredient, Recipe, Recipe_Ingredient
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
import json

# # def signin(request):

# @csrf_exempt
# def signup(request):
# 	if request.method != 'POST':
# 		return sendError('No post request')
# 	if request.POST.get('login', None) is None:
# 		return sendError('Login not defined')
# 	if request.POST.get('email', None) is None:
# 		return sendError('Email not defined')
# 	if request.POST.get('password', None) is None:
# 		return sendError('Password not defined')

# 	user = User.objects.create_user(request.POST['login'], 
# 							   request.POST['email'],
# 							   request.POST['password'])

# 	return sendResponse(json.dumps({'status': 'success', 'id': user.id}))

def home(request):
	"""Home page"""
	return render(request, 'nourriture/home.html', locals())

def ingredient(request, id):
	if int(id) <= 0:
		return sendError('Invalid ID')

	ingredient = Ingredient.objects.get(id=id)

	if ingredient is None:
		return sendError('Ingredient not found')

	response = serializeIngredient(ingredient)

	return sendResponse(json.dumps({'status': 'success', 'content': response}))

def ingredientAll(request):
	response = list()
	ingredients = Ingredient.objects.all()
	for ingredient in ingredients:
		response.append(serializeIngredient(ingredient))

	return sendResponse(json.dumps({'status': 'success', 'content': response}))

@csrf_exempt
@login_required(login_url='/accounts/login/')
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

	return sendResponse(json.dumps({'status': 'success', 'id': newIngredient.id}))

@csrf_exempt
#@login_required(login_url='/accounts/login/')
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

	return sendResponse(json.dumps({'status': 'success'}))

@csrf_exempt
#@login_required(login_url='/accounts/login/')
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

	return sendResponse(json.dumps({'status': 'success', 'id': ingredient.id}))

def recipe(request, id):
	# if request.method != 'POST':
	# 	return sendError('No post request')
	recipe = Recipe.objects.get(id=id)

	if recipe is None :
		return sendError('Recipe with id {} not found'.format(id))

	response = serializeRecipe(recipe)

	return sendResponse(json.dumps({'status': 'success', 'content': response}))

def recipeAll(request):
	recipes = Recipe.objects.all()

	response = list()

	for recipe in recipes:
		response.append(serializeRecipe(recipe))

	return sendResponse(json.dumps({'status': 'success', 'content': response}))

@csrf_exempt
#@login_required(login_url='/accounts/login/')
def recipeAdd(request):
	if request.method != 'POST':
		return sendError('No post request')

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

	return sendResponse(json.dumps({'status': 'success', 'id': newRecipe.id}))

@csrf_exempt
#@login_required(login_url='/accounts/login/')
def recipeDelete(request):
	if request.method != 'POST':
		return sendError('No post request')

	if request.POST['id'] is None:
		return sendError('Id not defined')

	recipe = Recipe.objects.get(id=request.POST['id'])

	if recipe:
		recipe.delete()
		rel = Recipe_Ingredient.objects.filter(recipe=recipe)
		rel.delete()
	else:
		return sendError('Id not found')

	return sendResponse(json.dumps({'status': 'success'}))

@csrf_exempt
#@login_required(login_url='/accounts/login/')
def recipeUpdate(request):
	if request.method != 'POST':
		return sendError('No post request')

	if request.POST['name'] is None:
		return sendError('Name not defined')

	if request.POST['id'] is None:
		return sendError('Id not defined')

	recipeIngredients = request.POST.getlist('ingredients', None)

	ingredientSet = checkIngredient(recipeIngredients)

	if ingredientSet is False:
		return sendError('Ingredients error')

	recipe = Recipe.objects.get(id=request.POST['id'])

	recipe.name = request.POST.get('name', "None")
	recipe.description = request.POST.get('description', None)

	rel = Recipe_Ingredient.objects.filter(recipe=recipe)
	rel.delete()

	recipe.save()

	for ingredient in ingredientSet:
		Recipe_Ingredient.objects.create(ingredient=ingredient,
										 recipe=recipe,
										 quantity=1)

	return sendResponse(json.dumps({'status': 'success', 'id': recipe.id}))



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

def serializeRecipe(recipe):
	response = dict()
	if recipe.name is not None:
		response['name'] = recipe.name
	if recipe.description is not None and len(recipe.description) > 0:
		response['description'] = recipe.description
	ingredients = recipe.ingredients.all()
	response['ingredients'] = list()
	for i,ingredient in enumerate(ingredients):
		ing = serializeIngredient(ingredient)
		ing['quantity'] = Recipe_Ingredient.objects.get(recipe=recipe, ingredient=ingredient).quantity
		response['ingredients'].append(ing)
	return response

def serializeIngredient(ingredient):
	response = dict()
	if ingredient.name is not None:
		response['name'] = ingredient.name
	if ingredient.description is not None and len(ingredient.description) > 0:
		response['description'] = ingredient.description
	if ingredient.price is not None:
		response['price'] = ingredient.price
	response['id'] = ingredient.id

	return response

def sendResponse(response, status=200):
	tosend = HttpResponse(response, status=status)
	tosend['Access-Control-Allow-Origin'] = "*"
	tosend['Access-Control-Allow-Methods'] = "*"
	tosend['Access-Control-Allow-Headers'] = "*"
	tosend["Access-Control-Max-Age"] = "100000"
	return tosend

def sendError(error=None, status=400):
	if error is None:
		return HttpResponse(json.dumps({'msg': 'error'}), status=status)
	else:
		return HttpResponse(json.dumps({'msg': 'error', 'error': error}), status=status)
