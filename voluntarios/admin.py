from django.contrib import admin
from .models import Voluntario

class VoluntarioAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'name', 'email', 'phone', 'join_date')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'name')

    # Search functionality
    search_fields = ('name',)

    #Rows per page to display
    list_per_page = 25

# Register your models here.
admin.site.register(Voluntario, VoluntarioAdmin)