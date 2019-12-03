from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Usuario
# Create your views here.
def registrarse(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usur = Usuario(nombre=form.cleaned_data['username'], direccion=form.cleaned_data['direccion'],numero=form.cleaned_data['numero'],correo=form.cleaned_data['correo'], ciudad='Bogota')
            usur.save()
            nombre = form.cleaned_data.get('username')
            return redirect('p-home')
    else:
        form = UserRegisterForm()
    return render(request, 'usuario/createUsuario.html', {'form': form})

