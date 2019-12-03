from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Usuarios

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        usur = Usuarios(user=instance, correo=instance.email, suscribirse=True)
        usur.save()
        print(usur)