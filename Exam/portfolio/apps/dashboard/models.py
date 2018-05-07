from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
########################################################################################################
class UsersManager(models.Manager):
	def register_validator(self, postData): 
		errors = {}
		first_name = postData['first_name']
		last_name = postData['last_name']
		email = postData['email']
		password = postData['password']
		password_c = postData['password_c'] 
		if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password) <1 or len(password_c)<1:
			errors['length'] = "All inputs must be filled"
			return errors 
		else:
			if len(first_name) < 3 or len(last_name) < 3:
				errors['name_length'] = "Name must be more than 2 characters"
			if not first_name.isalpha() or not last_name.isalpha():
				errors['name_type'] = "Name be alphabets only"
			if len(password) < 8 or len(password_c) < 8:
				errors['password_length'] = "Password be more than 8 characters"
			if password != password_c:
				errors['password_match'] = "Password confirmation failed"
			if not validate_email.match(email):
				errors['email_valid'] = "Email not valid"
			return errors		

	def login_validator(self, postData):
		errors ={}
		email = postData['login_id']
		login_password = postData['login_pw']
		
		if len(email)<1 or len(login_password)<1:
			errors['length'] = "All inputs must be filled"
			return errors
		else:
			user = Users.objects.filter(email = email)
			if not user:
				errors['invalid_id'] = "There is no record of this ID"
			else:
				user = Users.objects.get(email = email)
				data_password = user.password 
				if not bcrypt.checkpw(str(login_password).encode(), data_password.encode()):
					errors['invalid_password'] = "Invalid Password"
			return errors
########################################################################################################
class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	level = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add =True)
	objects = UsersManager()

class Boards(models.Model):
	user = models.OneToOneField(Users,related_name="users_board")

class Messages(models.Model):
	content = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add =True)
	user = models.ForeignKey(Users, related_name = "users_messages")
	board = models.ForeignKey(Boards, related_name = "boards_messages")

class Comments(models.Model):
	content = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add =True)
	message = models.ForeignKey(Messages, related_name ="messages_comments")
	user = models.ForeignKey(Users, related_name="users_comments")
	board = models.ForeignKey(Boards, related_name="boards_comments")

	