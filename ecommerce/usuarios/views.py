from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .forms import UserProfileForm

from .forms import UserForm


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
		form = UserForm(request.POST)
		if form.is_valid():
			print('La cuenta fue creada')
			form.save()
			return redirect('usuarios:login')
	else:
		form = UserForm()
	
	params['form'] = form
	
	return render(request, 'usuarios/register.html', params)


@login_required(login_url=reverse_lazy('usuarios:login'))
@transaction.atomic
def ver_datos(request):
	ctx = {}
	
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
		if user_form.is_valid() and user_profile_form.is_valid():
			user_form.save()
			user_profile_form.save()
			print('Form was saved')
			return redirect('usuarios:confirmacion-mis-datos')
	
	if request.method == 'GET':
		ctx['user_form'] = UserForm(instance=request.user)
		ctx['user_profile_form'] = UserProfileForm(instance=request.user.userprofile)
	
	return render(request, 'usuarios/mis-datos.html', ctx)


def confirmacion_mis_datos(request):
	return render(request, 'usuarios/editar-datos-confirmacion.html')
