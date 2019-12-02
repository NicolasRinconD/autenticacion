from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# Create your views here.
def registrarse(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('username')
            return redirect('p-home')
    else:
        form = UserRegisterForm()
    return render(request, 'usuario/createUsuario.html', {'form': form})