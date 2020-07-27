from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import Evento
from programacao.models import Programa
from evangelizacao.models import Evangelizacao
from eventos.choices import state_choices
from django.utils.translation import gettext

# Create your views here.
def index(request):
    # Render index template, shows 3 eventos only
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)[:3]
    programas = Programa.objects.order_by('-program_date').filter(is_published=True)[:4]
    evangelizacao = Evangelizacao.objects.order_by('-class_date').filter(is_published=True)[:4]
    
    context = {
        'programas': programas,
        'eventos': eventos,
        'evangelizacao': evangelizacao,
    }
    return render(request, 'pages/index.html', context)

def evangelizacao(request):
    # This is only needed if we had a separated page for
    evangelizacao = Evangelizacao.objects.order_by('-class_date').filter(is_published=True)
    context = {
        'evangelizacao': evangelizacao
    }
    return render(request, 'evangelizacao/evangelizacao.html', context)

def error_view_404(request, exception):
    return render(request, 'pages/404.html')

def error_view_500(request, exception):
    return render(request, 'pages/500.html')

def busca_eventos(request):
    # Render busca template
    return render(request, 'eventos/busca_eventos.html')

def busca_livros(request):
    # Render busca template
    return render(request, 'library/busca_livros.html')

def sobre(request):
    # Render sobre template
    return render(request, 'pages/sobre.html')

def assistencial(request):
    # Render assistencial template
    return render(request, 'pages/assistencial.html')

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