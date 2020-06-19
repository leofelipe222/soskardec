from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('wrnpro', ),
}

urlpatterns = [
    path('', include('pages.urls')), # This is for the Home Page
    path('eventos/', include('eventos.urls')), # This is a new app
    path('accounts/', include('accounts.urls')), # This is a new app
    path('contacts/', include('contacts.urls')), # This is a new app
    path('programacao/', include('programacao.urls')), # This is a new app
    # path('downloads/', include('downloads.urls')), # This is a new app
    path('rosetta/', include('rosetta.urls')), # translation library
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/', JavaScriptCatalog.as_view(), js_info_dict),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Setup media
