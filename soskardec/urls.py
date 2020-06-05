from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), # This is for the Home Page
    path('eventos/', include('eventos.urls')), # This is a new app
    path('accounts/', include('accounts.urls')), # This is a new app
    path('contacts/', include('contacts.urls')), # This is a new app
    path('downloads/', include('downloads.urls')), # This is a new app
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Setup media
