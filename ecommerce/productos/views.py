from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Producto


# Create your views here.
def home(request):
	return render(request, 'productos/index.html')


def login(request):
	return render(request, 'productos/login.html')


def register(request):
	return render(request, 'productos/register.html')


def hombres(request):
	params = {}
	productos = Producto.objects.filter(Q(genero='HOMBRES'), )
	params['productos'] = productos

	return render(request, 'productos/categoria-hombres.html', params)


def mujeres(request):
	params = {}
	productos = Producto.objects.filter(Q(genero='MUJERES'), )
	params['productos'] = productos
	return render(request, 'productos/categoria-mujeres.html', params)


def ninos(request):
	params = {}
	productos = Producto.objects.filter(Q(genero='NINOS'), )
	params['productos'] = productos
	return render(request, 'productos/categoria-ninos.html', params)