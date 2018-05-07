# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse 

# Create your views here.
def survey(request):
	return render(request, 'survey/survey.html')

def result(request):
	if request.method == 'POST':
		request.session['submit'] += 1
		name = request.POST['name']
		location = request.POST['location']
		language = request.POST['language']
		comment = request.POST['comment']
		context = {
			'trial':request.session['submit'],
			'name': name,
			'location': location,
			'language': language,
			'comment': comment
		}
		return render(request, 'survey/result.html', context)

def goback(request):
	return redirect('/survey')
