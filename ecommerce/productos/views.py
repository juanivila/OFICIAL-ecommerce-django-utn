from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'productos/index.html')


def login(request):
	return render(request, 'productos/login.html')


def register(request):
	return render(request, 'productos/register.html')


def categoria_hombres(request):
	return render(request, 'productos/categoria-hombres.html')
