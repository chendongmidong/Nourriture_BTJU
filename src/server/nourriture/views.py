from django.http import HttpResponse
from django.shortcuts import render

from django.core import serializers

from nourriture.models import Ingredient, Recipe

def home(request):
	"""Home page"""
	text = """<h1>Welcome on the nourriture API !</h1>
			  <h3>Routes (TODO):</h3>
			  /signin <br/>
			  /signup <br/>
			  /signout <br/>
			  /recipe/add <br/>
			  /recipe/delete <br/>
			  /recipe/update <br/>
			  /ingredient/view <br/>
			  /ingredient/add <br/>
			  /ingredient/delete <br/>
			  /ingredient/update <br/>
			  </p>"""
	return HttpResponse(text)
	# return render(request, text, locals())

def ingredientView(request):
	data = serializers.serialize("json", Ingredient.objects.all())

	return HttpResponse(data)

# def ingredientAdd(request):
# 	if request.method == 'POST'