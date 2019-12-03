from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=140, default='nr.normalemail@gmail.com')
    suscribirse = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} Perfil'