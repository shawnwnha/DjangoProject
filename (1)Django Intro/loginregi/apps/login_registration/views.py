from __future__ import unicode_literals
from django.shortcuts import render,redirect, HttpResponse 
from django.contrib import messages ######################### Django Flash
from .models import User
import bcrypt ############################################### Password Validation

def mainpage(request):
	return render(request, 'login_registration/main.html')

def register(request):
	errors = User.objects.registerValidator(request.POST)
	if len(errors):
		for k,v in errors.iteritems():
			messages.error(request, v, extra_tags =k)
		return redirect('/')

	else:
		request.session['first_name'] = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['pw']
		password_c = request.POST['pw_c']

		hash_password = bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())

		User.objects.create(first_name=request.session['first_name'], last_name=last_name,email=email,password=hash_password)
		return redirect('/success')

def success(request):
	context ={
		'name': request.session['first_name']
	}
	return render(request, 'login_registration/success.html', context)


def login(request):

	user_id = request.POST['login_id']	
	user_pw = request.POST['login_pw']

	user = User.objects.get(email = user_id)

	if not user:
		messages.error(request, "No id Matching in our system.")
		return redirect('/')
	else:
		password = user.password
		if bcrypt.checkpw(str(user_pw).encode(), password.encode()):
			request.session['first_name'] = user.first_name
			return redirect('/success')
		else:
			messages.error(request, "Password Incorrect.")
			return redirect('/')
