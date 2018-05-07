from __future__ import unicode_literals
from django.shortcuts import render, redirect 
from django.contrib import messages 
import bcrypt 
from .models import User, Book, Review
##########################################################################################
def loginpage(request):
	return render(request, 'initial_b/main.html')

def register(request):
	errors = User.objects.validator(request.POST)
	if len(errors):
		for k,v in errors.iteritems():
			messages.error(request,v, extra_tags=k)
		return redirect('/')
	
	else:
		request.session['name'] = request.POST['name']
		alias = request.POST['alias']
		email = request.POST['email']
		password = request.POST['password']
		hashed_pw = bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())

		User.objects.create(name=request.session['name'], alias =alias, email= email, password=hashed_pw)
		messages.success(request, "you have successfully registered")
		return redirect('/')

def login(request):
	login_id = request.POST['login_id']
	login_pw = request.POST['login_pw']

	user = User.objects.filter(email = login_id) 

	if not user:
		messages.error(request,"There is no record of this ID")
		return redirect('/')
	else:
		user = User.objects.get(email = login_id)
		password = user.password
		if bcrypt.checkpw(str(login_pw).encode(), password.encode()):
			request.session['name'] = user.name
			return redirect('/books')
		else:
			messages.error(request, "Password not matching")
			return redirect('/')
def logout(request):
	request.session['name'] = None
	return redirect('/')
##########################################################################################
def main(request):
	reviews= Review.objects.order_by('-created_at')[:3]
	reviews_rest = Review.objects.order_by('-created_at')[4:]
	context = {
		'reviews1': reviews,
		'reviews2': reviews_rest,
	}
	return render(request, "initial_b/book.html", context)

def addpage(request):
	return render(request, "initial_b/addbook.html")

def add(request):
	if len(request.POST['title']) < 1 or len(request.POST['review']) < 1:
		messages.error(request, "Input field cannot be empty!")
		return redirect('/books/add')
	else:
		title = request.POST['title']
		author = request.POST['author']
		review = request.POST['review']
		rating = request.POST['rating']

		user = User.objects.get(name = request.session['name'])

		book = Book.objects.create(title = title, author = author)

		review_created = Review.objects.create(review = review, rating = rating, reviewer = user, reviewed_book = book)
		return redirect('/books/{}'.format(book.id))
		
	
def show(request,book_id):
	request.session['book_id'] = book_id
	book = Book.objects.get(id = book_id)
	review = Review.objects.filter(reviewed_book = book)	
	context = {
		'books': book,
		'reviews' : review
	}
	print context
	return render(request, "initial_b/bookdetail.html", context)

def review(request):
	if len(request.POST['review']) < 1:
		messages.error(request,"Review cannot be empty!")
		return redirect('/books/{}'.format(request.session['book_id']))
	else:
		review = request.POST['review']
		rating = request.POST['rating']
		user = User.objects.get(name = request.session['name'])
		book = Book.objects.get(id = request.session['book_id'])
		Review.objects.create(review=review, rating =rating, reviewer = user, reviewed_book = book)
		return redirect('/books/{}'.format(request.session['book_id']))


def user(request,user_id):
	user = User.objects.get(id=user_id)
	user_reviews = Review.objects.filter(reviewer = user)
	count = user_reviews.count()
	context ={
		'user': user,
		'count': count,
		'user_reviews': user_reviews
	}

	return render(request, "initial_b/user.html", context)



# class User(models.Model):
# 	name = models.CharField(max_length=255)
# 	alias = models.CharField(max_length=255)
# 	email = models.EmailField()
# 	password = models.CharField(max_length=255)
# 	created_at = models.DateTimeField(auto_now_add =True)
# 	objects = UserManager()

# class Book(models.Model):
# 	title = models.CharField(max_length=255)
# 	author = models.CharField(max_length=255)

# class Review(models.Model):
# 	review = models.TextField()
# 	rating = models.IntegerField()
# 	reviewer = models.ForeignKey(User, related_name = "user_reviews")
# 	reviewed_book = models.ForeignKey(Book, related_name = "book_reviews")