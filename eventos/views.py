from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'eventos/eventos.html')

def evento(request):
    return render(request, 'eventos/evento.html')

def busca(request):
    return render(request, 'eventos/busca.html')

