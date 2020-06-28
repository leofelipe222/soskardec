from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='evangelizacao'), # This is /evangelizacao/ calling index method
]