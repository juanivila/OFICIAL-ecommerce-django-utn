from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from usuarios.models import DatosUsuario


@receiver(post_save, sender=User)
def create_datos_usuario(sender, instance, created, **kwargs):
	DatosUsuario.objects.create(usuario=instance)
	print('Se han los datos')


@receiver(post_save, sender=User)
def update_datos_usuario(sender, instance, created, **kwargs):
	if not created:
		instance.DatosUsuario.save()
		print('Se han actualizado los datos')
