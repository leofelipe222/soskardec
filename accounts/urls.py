from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('registrar', views.registrar, name='registrar'),
    path('logout', views.logout, name='logout'),
    path('usuario', views.usuario, name='usuario'),
]
