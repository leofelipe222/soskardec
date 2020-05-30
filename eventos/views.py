from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Evento

# Create your views here.
def index(request):
    # Fecth all eventos from DB, filter new ones first and is_published
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)

    # Adding pagination to the view
    paginator = Paginator(eventos, 6) # 5 items per page
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    
    context = {
        'eventos': paged_events
    }
    return render(request, 'eventos/eventos.html', context)

def evento(request, evento_id):
    return render(request, 'eventos/evento.html')

def busca(request):
    return render(request, 'eventos/busca.html')

