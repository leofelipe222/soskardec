from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Livro, Reserva

def library(request):
    # Fecth all classes from DB, filter new ones first and is_published
    books = Livro.objects.order_by('-title').filter(is_published=True)
    reservation = Reserva.objects.order_by('-title')

    # Adding pagination to the view
    paginator = Paginator(books, 8) # 10 books per page
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    
    context = {
        'books': paged_classes,
        'reservarion': reservation
    }
    return render(request, 'library/library.html', context)
