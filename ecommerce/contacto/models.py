from django.db import models


class Consulta(models.Model):
	email = models.EmailField()
	mensaje = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	respondido = models.BooleanField(default=False)
