from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Livro, Reserva

def index(request):
    # Fecth all classes from DB, filter new ones first and is_published
    books = Livro.objects.order_by('-title').filter(is_published=True)
    reservation = Reserva.objects.order_by('-title').filter(is_available=True)

    # Adding pagination to the view
    paginator = Paginator(books, 15) # 15 books per page
    page = request.GET.get('page')
    paged_books = paginator.get_page(page)
    
    context = {
        'books': paged_books,
        'reservarion': reservation
    }
    return render(request, 'library/library.html', context)

def busca_livros(request):


    # Adding query_set lists
    query_set_list = Livro.objects.order_by('-title').filter(is_published=True)
    # Filtering duplicated data for dropdownlist
    unique_authors = Livro.objects.values('author').distinct()
    unique_mediums = Livro.objects.values('medium').distinct()
    unique_publishers = Livro.objects.values('publisher').distinct()
    unique_languages = Livro.objects.values('language').distinct()

    # Keywords filter
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # Filter for any keyword passed by the user, not an exact match only
            query_set_list = query_set_list.filter(title__icontains=keywords)

    if 'author' in request.GET:
        author = request.GET['author']
        # Filter exact match only, case insensitive
        if author:
            query_set_list = query_set_list.filter(author__iexact=author)

    if 'medium' in request.GET:
        medium = request.GET['medium']
        # Filter exact match only, case insensitive
        if medium:
            query_set_list = query_set_list.filter(medium__iexact=medium)

    if 'publisher' in request.GET:
        publisher = request.GET['publisher']
        # Filter exact match only, case insensitive
        if publisher:
            query_set_list = query_set_list.filter(publisher__iexact=publisher)

    if 'language' in request.GET:
        language = request.GET['language']
        # Filter exact match only, case insensitive
        if language:
            query_set_list = query_set_list.filter(language__iexact=language)

    # Adding pagination to the view
    paginator = Paginator(query_set_list, 9) # 9 books per page
    query = request.GET
    page = request.GET.get('page')
    paged_books = paginator.get_page(page)

    context = {
        'books': paged_books,
        'unique_authors': unique_authors,
        'unique_mediums': unique_mediums,
        'unique_publishers': unique_publishers,
        'unique_languages': unique_languages,
        'query': query,
        'values': request.GET
    }
    return render(request, 'library/busca_livros.html', context)