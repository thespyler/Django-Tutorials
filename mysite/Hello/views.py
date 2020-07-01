from django.shortcuts import render
from django.http import HttpResponse
def sayHello(request):
	names = ['krishna', 'mukesh', 'Abhilash', 'harrison']
	return render(request, "main.html",
							{'names': names,
							 'game': 'Assasins Creed',
							 'fav_game': 'Gta 5',
							 'is_fav': True,
							 'is_not_fav': False
							})

def new_page(request):
	return render(request, 'test.html')

def new_hello(request, name):
	return HttpResponse("Hello" + name)

def login(request):
	name = request.POST['nm']
	password = request.POST['pass']
	return HttpResponse("Hello " + name + " your password is " + password)