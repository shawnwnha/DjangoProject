# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re # this is email validation! ###########################################
validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')####
#################################################################################

class UserManager(models.Manager):
	def registerValidator(self, postData):
		first_name = postData['first_name']
		last_name = postData['last_name']
		email = postData['email']
		password = postData['pw']
		password_c = postData['pw_c'] 

		errors = {}
		if len(first_name) < 3 or len(last_name) < 3:
			errors['name_length'] = "Name must be more than 2 characters"
		if not first_name.isalpha() or not last_name.isalpha():
			errors['name_type'] = "Name must be alphabets only"
		if len(password) < 8 or len(password_c) < 8:
			errors['password_length'] = "Password must be more than 8 characters"
		if password != password_c:
			errors['password_match'] = "Password confirmation failed"
		if not validate_email.match(email):
			errors['email_valid'] = "Email not valid"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


		# {% csrf_token %}
		# 	<label for="first_name">First Name: <input type ="text" name="first_name"></label><br>
		# 	<label for="last_name">Last Name: <input type ="text" name="last_name"></label><br>
		# 	<label for="email">Email: <input type ="text" name="email"></label><br>
		# 	<label for="pw">Password: <input type ="password" name="pw"></label><br>
		# 	<label for="pw_c">Confirm PW: <input type ="password" name="pw_c"></label><br>		
		# 	<input type="submit" value="Register">	