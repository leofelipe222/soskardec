from django.contrib import admin
from .models import Evangelizacao

class EvangelizacaoAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'title', 'is_published', 'class_date', 'class_type', 'volunteer')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'title', 'volunteer')

    # Creates a filter for the items below
    list_filter = ('title', 'class_type', 'volunteer')

    # Makes it editable
    list_editable = ('is_published',)

    # Search functionality
    search_fields = ('title', 'class_type', 'volunteer')

# Register your models here.
admin.site.register(Evangelizacao, EvangelizacaoAdmin)