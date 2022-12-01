from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DatosUsuario


class ContactoForm(forms.ModelForm):
	class Meta:
		model = DatosUsuario
		fields = ["nombre", "apellido", "imagen", "fecha_nacimiento", "pais", "provincia", "ciudad", "domicilio", "codigo_postal", "telefono", "dni", "cuit", ]


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
