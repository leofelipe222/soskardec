from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='eventos'), # This is /eventos/index
    path('<int:evento_id>', views.evento, name='evento'), # /eventos/id (23)
    path('busca', views.busca, name='busca')
]
