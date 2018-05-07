# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class user(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	def __repr__(self):
		return("user data: {},{},{},{},{}".format(self.first_name,self.last_name,self.email,self.created_at,self.updated_at))

class book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	uploader = models.ForeignKey(user, related_name = "uploaded_books")
	liked_users = models.ManyToManyField(user, related_name = "liked_books")

	def __repr__(self):
		return("book data: {},{},{},{}".format(self.name,self.desc,self.created_at,self.updated_at))
