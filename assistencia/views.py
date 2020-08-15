from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import Assistencia

# Create your views here.
def assistencia(request):
    # Fecth all classes from DB, filter new ones first and is_published
    donations = Assistencia.objects.order_by('demmand').filter(is_published=True)
    context = {
        'donations': donations
    }

    return render(request, 'pages/assistencia.html', context)