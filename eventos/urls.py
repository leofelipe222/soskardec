from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='eventos'), # This is /eventos/ calling index method
    path('<int:evento_id>', views.evento, name='evento'), # /eventos/id (23)
    path('busca_eventos', views.busca_eventos, name='busca_eventos'),
]
