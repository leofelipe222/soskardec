from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Evento
from eventos.choices import state_choices

# Create your views here.
def index(request):
    # Fecth all eventos from DB, filter new ones first and is_published
    eventos = Evento.objects.order_by('-event_date').filter(is_published=True)

    # Adding pagination to the view
    paginator = Paginator(eventos, 6) # 6 items per page
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    
    context = {
        'eventos': paged_events
    }
    return render(request, 'eventos/eventos.html', context)

def evento(request, evento_id):
    # Shows the 404 error if there is no page
    evento = get_object_or_404(Evento, pk=evento_id)

    context = {
        'evento': evento
    }

    return render(request, 'eventos/evento.html', context)

def busca_eventos(request):

    # Adding query_set lists
    query_set_list = Evento.objects.order_by('-event_date').filter(is_published=True)

    # Keywords filter
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # Filter for any keyword passed by the user, not an exact match only
            query_set_list = query_set_list.filter(description__icontains=keywords)
        # print(query_set_list)

    if 'city' in request.GET:
        city = request.GET['city']
        # Filter exact match only, case insensitive
        if city:
            query_set_list = query_set_list.filter(city__iexact=city)
        

    if 'state' in request.GET:
        state = request.GET['state']
        # Filter exact match only, case insensitive
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)

    # Adding pagination to the view
    paginator = Paginator(query_set_list, 9) # 9 events per page
    query = request.GET
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)

    context = {
        'state_choices': state_choices,
        'eventos': paged_events,
        'query': query,
        'values': request.GET
    }
    return render(request, 'eventos/busca_eventos.html', context)

