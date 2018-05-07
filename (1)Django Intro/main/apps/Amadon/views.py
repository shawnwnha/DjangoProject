# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse 

def main(request):	
	if 'cart' not in request.session:
		request.session['cart'] = []
	return render(request, 'Amadon/Amadon.html')

def order(request):


	if 	int(request.POST['product_id']) == 1111:
		item = 'Dojo Tshirt'
		price = 19.99
		amount = request.POST['quantity']


	if int(request.POST['product_id']) == 2222:
		item = 'Dojo Sweater'
		price = 29.99
		amount = request.POST['quantity']

	if int(request.POST['product_id']) == 3333:
		item = 'Dojo Cup'
		price = 4.99
		amount = request.POST['quantity']

	if int(request.POST['product_id']) == 4444:
		item = 'Algorithm Book'
		price = 49.99
		amount = request.POST['quantity']

	cart = {
		'item' : item,
		'price': price,
		'amount': amount
	}	

	temp_list = request.session['cart']
	temp_list.append(cart)
	request.session['cart'] = temp_list 

	return redirect('/amadon/checkout')

def checkout(request):
	total_cost = 0
	total_amount = 0
	for cart in range(0,len(request.session['cart'])):
		total_cost += (request.session['cart'][cart]['price']*int(request.session['cart'][cart]['amount']))
		total_amount += int(request.session['cart'][cart]['amount'])
		print total_cost
		print total_amount

	checkout_cost = request.session['cart'][len(request.session['cart'])-1]['price'] * int(request.session['cart'][len(request.session['cart'])-1]['amount'])
	print checkout_cost

	context ={
		'total_cost': total_cost,
		'checkout_cost': checkout_cost,
		'total_amount': total_amount,
	}

	return render(request, 'Amadon/success.html', context)