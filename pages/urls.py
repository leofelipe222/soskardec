from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This is the home page path
    path('about', views.about, name='about') # This takes you to the about page
]
