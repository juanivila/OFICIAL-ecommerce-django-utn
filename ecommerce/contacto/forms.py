from django import forms
from captcha.fields import CaptchaField
from .models import Consulta


class ContactoForm(forms.ModelForm):
	captcha = CaptchaField()
	
	class Meta:
		model = Consulta
		fields = ['email', 'mensaje']
