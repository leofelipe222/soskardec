from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import Evento
from programacao.models import Programa
from evangelizacao.models import Evangelizacao
from assistencia.models import Assistencia
from eventos.choices import state_choices
from django.utils.translation import gettext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    # Render index template, shows 3 eventos only
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)[:3]
    programas = Programa.objects.order_by('program_date').filter(is_published=True)[:4]
    evangelizacao = reversed(Evangelizacao.objects.order_by('-class_date').filter(is_published=True)[:4])
    
    context = {
        'programas': programas,
        'eventos': eventos,
        'evangelizacao': evangelizacao,
    }
    return render(request, 'pages/index.html', context)

def evangelizacao(request):
    # Fecth all classes from DB, filter new ones first and is_published
    evangelizacao = Evangelizacao.objects.all().order_by('-class_date').filter(is_published=True)

    # Adding pagination to the view
    paginator = Paginator(evangelizacao, 10) # 10 items per page
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    
    context = {
        'evangelizacao': paged_classes
    }
    return render(request, 'evangelizacao/evangelizacao.html', context)

# Create your views here.
def assistencia(request):
    # Fecth all classes from DB, filter new ones first and is_published
    donations = Assistencia.objects.order_by('demmand').filter(is_published=True)
    context = {
        'donations': donations
    }

    return render(request, 'pages/assistencia.html', context)

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