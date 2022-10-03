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


def categoria_hombres(request):
	params = {}
	productos = Producto.objects.filter(Q(genero='HOMBRES'), )
	params['productos'] = productos
	print(params)
	return render(request, 'productos/categoria-hombres.html', params)
