from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This is the home page path
    path('sobre', views.sobre, name='sobre'),
    path('assistencial', views.assistencial, name='assistencial'),
    path('assistencia', views.assistencia, name='assistencia'),
    path('espiritismo', views.espiritismo, name='espiritismo'),
    path('atividades', views.atividades, name='atividades'),
    path('eventos', views.eventos, name='eventos'),
    # path('programacao', views.programacao, name='programacao'),
    # path('contacts', views.contacts, name='contacts'),
    # path('downloads', views.downloads, name='downloads'),
    path('evangelizacao', views.evangelizacao, name='evangelizacao'),
    path('busca_eventos', views.busca_eventos, name='busca_eventos'),
    path('busca_livros', views.busca_livros, name='busca_livros'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login, name='login')
]
