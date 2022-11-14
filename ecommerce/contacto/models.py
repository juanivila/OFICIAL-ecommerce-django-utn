from django.db import models


class Consulta(models.Model):
	email = models.EmailField()
	mensaje = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	respondido = models.BooleanField(default=False)
	
	def __str__(self):
		return self.email


class Respuesta(models.Model):
	consulta = models.ForeignKey(Consulta, blank=True, null=True, on_delete=models.CASCADE)
	respuesta = models.TextField(blank=False, null=False)
	fecha = models.DateTimeField(auto_now_add=True, blank=True, editable=True)
	
	def create_mensaje(self):
		consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
		consulta_cambio_estado.respondido = True
		consulta_cambio_estado.save()
	
	def save(self, *args, **kwargs):
		self.create_mensaje()
		force_update = False
		if self.id:
			force_update = True
		
		super(Respuesta, self).save(force_update=force_update)
