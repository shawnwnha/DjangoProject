# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse 
from django.contrib import messages 
from .models import Course 

# Create your views here.
def main(request):
	courses = Course.objects.all()
	context = {
		'courses': courses 
	}
	return render(request, 'validation/main.html',context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	
	if len(errors):
		for tag,v in errors.iteritems():
			messages.error(request, v, extra_tags = tag) ######this is way of using messages.
		return redirect('/')

	else:
		name = request.POST['name_input']
		desc = request.POST['desc_input']
		Course.objects.create(name=name,description=desc)
		return redirect('/') 

def deletepage(request, id):
	x = Course.objects.get(id = id)
	context = {
		'id': x.id,
		'name': x.name,
		'description' : x.description 
	}
	return render(request, 'validation/delete.html',context)

def delete(request,id):
	if request.POST['hidden'] == 'no':
		return redirect('/')
	else:
		course_delete = Course.objects.get(id=id)
		course_delete.delete()
		return redirect('/')