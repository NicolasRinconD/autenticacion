from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    correo = forms.EmailField(max_length=35)
    numero = forms.IntegerField()
    direccion = forms.CharField(max_length=60)
    class Meta:
        model = User
        fields = ['username', 'correo', 'numero', 'direccion', 'password1', 'password2']