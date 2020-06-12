from django.urls import path
from . import views

urlpatterns = [
    path('programacao', views.index, name='programacao')
]