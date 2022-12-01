from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import ContactoForm
from usuarios.models import DatosUsuario

from .forms import CreateUserForm


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
			return render(request, 'usuarios/login.html', params)
	
	return render(request, 'usuarios/login.html')


def logout_page(request):
	logout(request)
	return redirect(reverse('productos:home'))


def register(request):
	params = {}
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			print('La cuenta fue creada')
			form.save()
			return redirect('usuarios:login')
	else:
		form = CreateUserForm()
	
	params['form'] = form
	
	return render(request, 'usuarios/register.html', params)


@login_required(login_url=reverse_lazy('usuarios:login'))
def editar_datos(request):
	params = {
		'user': request.user,
		"email": request.user.email,
		}
	if request.method == 'GET':
		form = ContactoForm()
		params['form'] = form
	
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			print('Form is valid!')
			print(form)
			form.save()
			request.session['nombre'] = form.cleaned_data['nombre']
			return redirect(reverse_lazy('usuarios:confirmacion-mis-datos'))
	
	return render(request, 'usuarios/editar-datos.html', params)


def confirmacion_mis_datos(request):
	return render(request, 'usuarios/editar-datos-confirmacion.html')
