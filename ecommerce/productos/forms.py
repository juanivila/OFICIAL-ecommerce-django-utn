from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Producto


class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'
		exclude = ('fecha_agregado',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
