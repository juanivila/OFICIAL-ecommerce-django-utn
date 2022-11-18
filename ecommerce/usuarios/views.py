from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from usuarios.models import DatosUsuario


@login_required(login_url=reverse_lazy('productos:login'))
def mis_datos(request):
	params = {
		'user': request.user,
		"email": request.user.email,
		}
	
	return render(request, 'usuarios/mis-datos.html', params)
