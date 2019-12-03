from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=90, blank=False)
    direccion = models.CharField(max_length=90, blank=False)
    numero = models.IntegerField(blank=False)
    ciudad = models.CharField(max_length=50, blank=False)
    correo = models.EmailField(max_length=140, default='nr.normalemail@gmail.com')

    def __str__(self):
        return f'{self.correo} Perfil'