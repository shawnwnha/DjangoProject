# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse 

def index(request):
	return HttpResponse("placeholder to later display all the list of blogs")
def new(request):
	return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
	return redirect('/blogs')
def show(request,number):
	str = 'placeholder to display blog ' + number # number* type = unicode 
	return HttpResponse(str)
def edit(request,number):
	str = 'placeholder to display blog ' + number # number* type = unicode 
	return HttpResponse(str)
def destroy(request,number):
	return redirect('/blogs')