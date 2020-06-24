from django.contrib import admin
from .models import Programa

class ProgramaAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'title', 'is_published', 'program_date', 'program_type', 'volunteer', 'language', 'description')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'title', 'volunteer')

    # Creates a filter for the items below
    list_filter = ('title', 'program_type', 'program_date', 'volunteer')

    # Makes it editable
    list_editable = ('is_published',)

    # Search functionality
    search_fields = ('title', 'description', 'volunteer', 'program_type', 'language')

# Register your models here.
admin.site.register(Programa, ProgramaAdmin)
