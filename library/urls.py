from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library'),
    path('busca_livros', views.busca_livros, name='busca_livros'),
]
