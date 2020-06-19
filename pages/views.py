from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import Evento
from programacao.models import Programa
from eventos.choices import state_choices
from django.utils.translation import gettext

# Create your views here.
def index(request):
    # Render index template, shows 3 eventos only
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)[:3]

    programas = Programa.objects.order_by('-program_date').filter(is_published=True)
    
    context = {
        'programas': programas,
        'eventos': eventos
    }
    return render(request, 'pages/index.html', context)


# def programacao(request):
#     # This is only needed if we had a separated page for
#     programas = Programa.objects.order_by('-program_date').filter(is_published=True)
#     context = {
#         'programas': programas
#     }
#     return render(request, 'pages/index.html', context)

def busca(request):
    # Render busca template
    return render(request, 'eventos/busca.html')

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