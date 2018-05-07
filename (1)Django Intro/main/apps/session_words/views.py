# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse 
from time import gmtime, strftime

def main(request):
	if 'property' not in request.session:
		request.session['property'] = []

	return render(request, 'session_words/words.html')

def result(request):
	print request.POST
	if 'newword' not in request.POST:
		text = " "
	else:
		text = request.POST['newword']


	if 'color' not in request.POST:
		color="black;"
	else: 
		color = request.POST['color'] 

	if 'font' not in request.POST:
		font = "12px;"

	else:
		font = request.POST['font']
	
	time = strftime("%Y-%m-%d %H:%M %p", gmtime())

	temp_dict = {
		'color': color,
		'font': font,
		'text': text,
		'time': time
	}

	session_list = request.session['property']
	session_list.append(temp_dict)
	request.session['property'] = session_list
	context={
		'property': request.session['property']
	}

	print request.session['property']
	return render(request, 'session_words/words.html', context)

def delete(request):
	del request.session['property']
	return redirect('/session')