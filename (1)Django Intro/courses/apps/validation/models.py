# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def basic_validator(self,postData):
		errors ={}
		if len(postData['name_input']) < 5:
			errors['name'] = "Course name should be more than 5 characters"
		if len(postData['desc_input']) <10:
			errors['desc'] = "Desciption shoud be more than 10 characters"

		return errors 

class Course(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = CourseManager()