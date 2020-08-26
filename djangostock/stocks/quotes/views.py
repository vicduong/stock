from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
def home(request):
	import requests
	import json 


	if request.method =='POST':
		ticker = request.POST['ticker']
		# pk_910426c527d64e168a721f776ef3e28a
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote/?token=pk_910426c527d64e168a721f776ef3e28a")

		try:
			api = json.loads(api_request.content) # return save apit get on requests
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})
	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json 

	if request.method =='POST': # fill out form click button
		form = StockForm(request.POST or None) # var store - passing request post - pass value in StockForm
		
		if form.is_valid(): # not empty
			form.save() # save to database
			messages.success(request, ("Stock Has Been Added!"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote/?token=pk_910426c527d64e168a721f776ef3e28a")
			try:
				api = json.loads(api_request.content) # return save apit get on requests
				output.append(api)
				#every time loop through item - return a dictionary many info keys
				#need to store each item dict in list 
				#append=add item to list

			except Exception as e:
				api = "Error..."
		#now we pass that list in our page 
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output}) #key value

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})