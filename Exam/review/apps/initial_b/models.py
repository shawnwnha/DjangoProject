from __future__ import unicode_literals
from django.db import models
import re

validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validator(self,postData):
		name = postData['name']
		alias = postData['alias']
		email = postData['email']
		password = postData['password']
		password_c = postData['password_c'] 

		errors = {}
		if len(name) < 3 or len(alias) < 3:
			errors['name_length'] = "Name or Alias must be more than 2 characters"
		if not name.isalpha() or not alias.isalpha():
			errors['name_type'] = "Name  or Alias must be alphabets only"
		if len(password) < 8 or len(password_c) < 8:
			errors['password_length'] = "Password must be more than 8 characters"
		if password != password_c:
			errors['password_match'] = "Password confirmation failed"
		if not validate_email.match(email):
			errors['email_valid'] = "Email not valid"

		return errors

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add =True)
	objects = UserManager()

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)

class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	reviewer = models.ForeignKey(User, related_name = "user_reviews")
	reviewed_book = models.ForeignKey(Book, related_name = "book_reviews")
	created_at = models.DateTimeField(auto_now_add = True)