from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Profil

import json

@csrf_exempt
def signup(request):
	if request.method != 'POST':
		return sendError('No post request')
	elif request.POST.get('login', None) is None:
		return sendError('Login not defined')
	elif request.POST.get('email', None) is None:
		return sendError('Email not defined')
	elif request.POST.get('password', None) is None:
		return sendError('Password not defined')

	if request.POST.get('role', None) is None or request.POST['role'] == 'consumer':
		group = Group.objects.get(name='consumer')
	elif request.POST['role'] == 'gastronomist':
		group = Group.objects.get(name='gastronomist')
	elif request.POST['role'] == 'supplier':
		group = Group.objects.get(name='supplier')
	else :
		return sendError('Invalid Role')

	user = User.objects.create_user(request.POST['login'], 
							   request.POST['email'],
							   request.POST['password'])
	user.groups.add(group)
	user.save()

	profil = Profil.objects.create(user=user)

	return sendResponse(json.dumps({'status': 'success', 'id': user.id}))

@csrf_exempt
# @require_http_methods(["POST"])
def login(request):
	username = request.POST.get('username', None)
	password = request.POST.get('password', None)
	user = authenticate(username=login, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return sendResponse({'status': 'success', 'id': user.id})
		else:
			return sendError('User account dissabled')
	else:
		return sendError('Invalid login')

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

