from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import Evento
from eventos.choices import state_choices

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def busca(request):
    # Render index template, shows 3 eventos only
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)

    context = {
        'state_choices': state_choices,
        'eventos': eventos,
    }

    return render(request, 'eventos/busca.html', context)

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