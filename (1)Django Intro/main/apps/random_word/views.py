# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse 
from django.utils.crypto import get_random_string 


def main(request):
	request.session['trial'] = 0
	return render(request, 'random_word/random_word.html',)

def create(request):
	if request.method == 'POST':
		context = {
			'trial': request.session['trial'],
			'random_word': get_random_string(length =14)
		}
		request.session['trial'] += 1
		return render(request, 'random_word/random_word.html', context)
