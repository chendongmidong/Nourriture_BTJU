from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

from django.core import serializers

import json

from nourriture.models import Ingredient, Recipe

def home(request):
	"""Home page"""
	return render(request, 'nourriture/home.html', locals())

def ingredientView(request):
	response = serializers.serialize("json", Ingredient.objects.all())

	return HttpResponse(response)

@csrf_exempt
def ingredientAdd(request):
	if request.method != 'POST':
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	if request.POST['name'] is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	newIngredient = Ingredient(name=request.POST.get('name', "None"),
							   description=request.POST.get('description', None),
							   price=request.POST.get('price', None))

	newIngredient.save()

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success', 'id': newIngredient.id}))

@csrf_exempt
def ingredientDelete(request):
	if request.method != 'POST':
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	if request.POST['id'] is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	ingredient = Ingredient.objects.filter(id=request.POST['id'])

	if ingredient:
		ingredient.delete()
	else:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success'}))

@csrf_exempt
def ingredientUpdate(request):
	if request.method != 'POST':
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	if request.POST['name'] is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	if request.POST['id'] is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	ingredient = Ingredient.objects.filter(id=request.POST['id'])

	if ingredient is None:
		return HttpResponse(json.JSONEncoder().encode({'msg': 'error'}))

	ingredient.name = request.POST.get('name', "None")
	ingredient.description = request.POST.get('description', None)
	ingredient.price = request.POST.get('price', None)

	ingredient.save()

	return HttpResponse(json.JSONEncoder().encode({'msg': 'success', 'id': ingredient.id}))


