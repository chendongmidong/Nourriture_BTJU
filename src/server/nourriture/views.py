from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

from django.core import serializers

import json

from nourriture.models import Ingredient, Recipe

def home(request):
	"""Home page"""
	text = """<h1>Welcome on the nourriture API !</h1>
			  <h2>Routes (TODO):</h2>
			  /signin <br/>
			  /signup <br/>
			  /signout <br/>
			  /recipe/add <br/>
			  /recipe/delete <br/>
			  /recipe/update <br/>
			  /ingredient/view (Done) GET<br/>
			  <pre>
[
	{
		model: "nourriture.ingredient",
		pk: 1,
		fields: {
			description: "de bon gros oeufs !",
			name: "Egg",
			price: 1
		}
	},
	{
		model: "nourriture.ingredient",
		pk: 2,
		fields: {
			description: "De la farine ma gueule",
			name: "Flour",
			price: 3
		}
	}
]
			  </pre>
			  /ingredient/add (Done)<br/>
			  /ingredient/delete <br/>
			  /ingredient/update <br/>
			  </p>"""
	return HttpResponse(text)
	# return render(request, text, locals())

def ingredientView(request):
	response = serializers.serialize("json", Ingredient.objects.all())

	return HttpResponse(response)

@csrf_exempt
def ingredientAdd(request):
	if request.method != 'POST':
		data = {'msg':'error'}
		response = json.JSONEncoder().encode(data)
		return HttpResponse(response)

	if request.POST['name'] is None:
		data = {'msg':'error'}
		response = json.JSONEncoder().encode(data)
		return HttpResponse(response)

	newIngredient = Ingredient(name=request.POST.get('name', None),
							   description=request.POST.get('description', None),
							   price=request.POST.get('price', None))

	newIngredient.save()
	print (newIngredient.id)
	return HttpResponse(json.JSONEncoder().encode({'msg': 'success'}))

