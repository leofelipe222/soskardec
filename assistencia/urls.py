from django.urls import path
from . import views

urlpatterns = [
    path('assitencia', views.assitencia, name='assitencia')
]