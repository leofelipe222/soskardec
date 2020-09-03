from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Evangelizacao

# Create your views here.
def index(request):
    # This is only needed if we had a separated page for
    evangelizacao = Evangelizacao.objects.order_by('class_date').filter(is_published=True)
    context = {
        'evangelizacao': evangelizacao
    }
    return render(request, 'evangelizacao/evangelizacao.html', context)
