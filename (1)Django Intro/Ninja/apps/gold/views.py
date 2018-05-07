# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse 
from time import gmtime, strftime
import random

def main(request):
	if 'log' not in request.session:
		request.session['log'] = []

	if 'score' not in request.session:
		request.session['score'] = 0

	return render(request,'gold/gold.html')

def money(request):
	if request.POST['hidden'] == 'farm':
		score = random.randint(10,20)
	elif request.POST['hidden'] == 'cave':
		score = random.randint(5,10)
	elif request.POST['hidden'] == 'house':
		score = random.randint(2,5)
	elif request.POST['hidden'] == 'casino':
		score_set = random.randint(0,1)
		if score_set == 0:
			score = -random.randint(0,50) 
		else:
			score = random.randint(0,50) 
	
	time = strftime("%Y-%m-%d %H:%M %p", gmtime())

	request.session['score'] += score
	activities = {
		'score': score,
		'time' : time, 
		'location': request.POST['hidden']
	}

	temp = request.session['log']
	temp.append(activities)

	request.session['log'] = temp

	print request.session['log']
	return render(request, 'gold/gold.html')