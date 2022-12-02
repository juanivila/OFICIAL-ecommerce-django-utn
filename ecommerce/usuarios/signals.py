from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_datos_usuario(sender, instance, created, **kwargs):
	if created:
		print(f"Instance: {instance}")
		UserProfile.objects.create(usuario=instance)
		print('Se han creado los datos.')
