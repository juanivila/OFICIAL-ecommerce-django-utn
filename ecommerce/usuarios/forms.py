from django import forms

from .models import DatosUsuario


class ContactoForm(forms.ModelForm):
	class Meta:
		model = DatosUsuario
		fields = ["nombre", "apellido", "imagen", "fecha_nacimiento", "pais", "provincia", "ciudad", "domicilio", "codigo_postal", "telefono", "dni", "cuit", ]
