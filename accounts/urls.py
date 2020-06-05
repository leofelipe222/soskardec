from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('registrar', views.registrar, name='registrar'),
    path('logout', views.logout, name='logout'),
    path('painel_usuario', views.painel_usuario, name='painel_usuario'),
]
