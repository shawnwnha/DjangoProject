# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def first(request):
	return HttpResponse("placeholder to display all the surveys created")
def second(request):
	return HttpResponse("placeholder for users to add a new survey")