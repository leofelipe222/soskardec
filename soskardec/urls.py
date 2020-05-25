from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), # This is for the Home Page
    path('eventos/', include('eventos.urls')), # This is a new app
    path('admin/', admin.site.urls),
]
