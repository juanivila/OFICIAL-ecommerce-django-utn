from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CreateUserForm, ProductoForm
from .models import Producto


# Create your views here.
def home(request):
	return render(request, 'productos/index.html')


def login_page(request):
	params = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			print(username)
			print(password)
			login(request, user)
			return redirect('productos:home')
		else:
			print('There was an error ')
			return render(request, 'productos/login.html', params)
	
	return render(request, 'productos/login.html')


def register(request):
	params = {}
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print('La cuenta fue creada')
			form.save()
			return redirect('productos:login')
	else:
		form = CreateUserForm()
	
	params['form'] = form
	
	return render(request, 'productos/register.html', params)


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


class AgregarProducto(CreateView):
	template_name = 'productos/agregar-producto.html'
	form_class = ProductoForm
	success_url = reverse_lazy('agregar-producto-success')


class AgregarProductoSuccess(TemplateView):
	template_name = 'productos/agregar-producto-success.html'
