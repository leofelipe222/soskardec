from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Evangelizacao

# Create your views here.
def index(request):
    # Fecth all classes from DB, filter new ones first and is_published
    evangelizacao = Evangelizacao.objects.order_by('-class_date').filter(is_published=True)

    # Adding pagination to the view
    paginator = Paginator(evangelizacao, 6) # 6 items per page
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    
    context = {
        'evangelizacao': paged_classes
    }
    return render(request, 'evangelizacao/evangelizacao.html', context)