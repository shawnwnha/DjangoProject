# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User


def index(request): # shows firstpage where all user logs are shown
	if len(User.objects.all()):
		users = User.objects.all()
		context ={
			'users': users,
		}
		print User.objects.all()
		return render(request, 'semi_users/index.html', context)

	else:
		return render(request,'semi_users/index.html')
		
def new(request): # shows new registration page
	return render(request, 'semi_users/new.html')

def create(request): # handles new registration page
	if len(request.POST):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']

		user = User.objects.create(first_name = first_name, last_name = last_name, email = email)
		print user.id

	return redirect('/users/'+str(user.id))

def show(request,id): #shows a single user info page
	user = User.objects.get(id = id)
	context ={
		'user_id': user.id,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'created_at': user.created_at,
	}

	return render(request,'semi_users/user.html', context)

def edit(request,id): # shows a single user edit page
	user_id = id 
	context ={
		'user_id': user_id
	}
	return render(request, 'semi_users/edit.html',context)

def update(request,id): # handles a edit logic
	print "!"
	user = User.objects.get(id = id)
	if len(request.POST):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		
		user.first_name = first_name
		user.last_name = last_name 
		user.email = email 
		user.save()
		
		context ={
			'user_id': user.id,
			'first_name': user.first_name,
			'last_name': user.last_name,
			'email': user.email,
			'created_at': user.created_at,
		}

	return redirect('/users/{}'.format(user.id))

def destroy(request,id): # handles delete user logic
	user = User.objects.get(id = id)
	user.delete()
	return redirect('/users')