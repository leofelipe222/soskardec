from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This is the home page path
    path('sobre', views.sobre, name='sobre'),
    path('espiritismo', views.espiritismo, name='espiritismo'),
    path('atividades', views.atividades, name='atividades'),
    path('eventos', views.eventos, name='eventos'),
    # path('programacao', views.programacao, name='programacao'),
    # path('contacts', views.contacts, name='contacts'),
    path('busca', views.busca, name='busca'),
    path('downloads', views.downloads, name='downloads'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login, name='login')
]
