from django.http import HttpResponse
from django.shortcuts import render

def tillte_page(request):
    return HttpResponse('<H1> Smart solutions: estamos en desarrollo...</h1>')
def index(request):
    return render(request, 'index.html')
