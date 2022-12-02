from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
	usuario = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to="producto/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	
	def __str__(self):
		try:
			return self.usuario.username
		
		except AttributeError:
			return f"{self.nombre} {self.apellido}"
