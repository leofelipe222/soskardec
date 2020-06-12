from django.shortcuts import render
from .models import Programa

# Create your views here.
def index(request):
    # Fecth all eventos from DB, filter new ones first and is_published
    programas = Programa.objects.all().filter(is_published=True)

    context = {
        'programas': programas
    }
    return render(request, 'pages/index.html', context)
