from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Render index template
    return render(request, 'pages/index.html')

def sobre(request):
    # Render sobre template
    return render(request, 'pages/sobre.html')

def espiritismo(request):
    return render(request, 'pages/espiritismo.html')

def atividades(request):
    return render(request, 'pages/atividades.html')

def eventos(request):
    return render(request, 'pages/eventos.html')

def downloads(request):
    return render(request, 'pages/downloads.html')

def registrar(request):
    return render(request, 'pages/registrar.html')

def login(request):
    return render(request, 'pages/login.html')