from __future__ import unicode_literals
from django.shortcuts import render, redirect 
from django.contrib import messages 
from .models import Users,Boards,Messages,Comments 
import bcrypt 

def welcomepage(request):
	return render(request, 'dashboard/firstpage.html')

def loginpage(request):
	return render(request,'dashboard/loginpage.html')

def registerpage(request):
	return render(request, 'dashboard/registerpage.html')

def register(request):
	errors = Users.objects.register_validator(request.POST)
	if len(errors):
		for tag, content in errors.iteritems():
			messages.error(request,content,extra_tags=tag)
		return redirect('/register')
	else:
		if not Users.objects.all():
			level = 9
		else: 
			level = 0 

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		hashed_pw = bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())
		Users.objects.create(first_name=first_name, last_name =last_name, email= email, password=hashed_pw, level = level)
		messages.success(request, "you have successfully registered")
		return redirect('/login')

def login(request):
	errors = Users.objects.login_validator(request.POST)
	if len(errors):
		for tag, content in errors.iteritems():
			messages.error(request, content, extra_tags=tag)
		return redirect('/login')
	else:
		user = Users.objects.get(email = request.POST['login_id'])
		request.session['id'] = user.id ########### SAVE SESSION['ID'] ON LOGIN 
		request.session['level'] = user.level

		if request.session['level'] == 9:
			return redirect('/dashboard/admin')
		else:
			return redirect('/dashboard')

##################################################################################

def dashboard(request):
	users = Users.objects.all()
	context = {
		'users': users
	}
	return render(request, 'dashboard/dashboard.html', context)


def adminboard(request):
	if request.session['level'] != 9: ##to prevent users accessig abnormal path
		return redirect('/dashboard')
	else:	
		users = Users.objects.all()
		context = {
			'users': users
		}
		return render(request, 'dashboard/dashboard.html', context)


##################################################################################

def show(request, id):
	user = Users.objects.get(id =id)
	board = Boards.objects.get(user = user)
	messages = Messages.objects.filter(board = board)
	comments = Comments.objects.filter(message = messages).order_by('-created_at')
	
	print comments

	context = {
		'user' : user,
		'messages' : messages,
		'comments': comments
	}

	return render(request,'dashboard/userinfo.html',context)