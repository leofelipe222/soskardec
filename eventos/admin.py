from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'title', 'is_published', 'event_date', 'event_type', 'address', 'city', 'volunteer')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'title', 'volunteer')

    # Creates a filter for the items below
    list_filter = ('title', 'event_type', 'volunteer')

    # Makes it editable
    list_editable = ('is_published',)

    # Search functionality
    search_fields = ('title', 'description', 'volunteer', 'event_type')

# Register your models here.
admin.site.register(Evento, EventoAdmin)