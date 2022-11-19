from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ContactoForm
from usuarios.models import DatosUsuario


@login_required(login_url=reverse_lazy('productos:login'))
def mis_datos(request):
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
	
	return render(request, 'usuarios/mis-datos.html', params)


def confirmacion_mis_datos(request):
	return render(request, 'usuarios/mis-datos-confirmacion.html')
