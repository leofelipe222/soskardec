from django.contrib import admin
from .models import Livro, Reserva

class LibraryAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'code', 'title', 'is_published', 'author', 'medium', 'publisher', 'copies', 'language', 'volunteer')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'code', 'title', 'author', 'medium', 'publisher')

    # Creates a filter for the items below
    list_filter = ('author', 'medium', 'publisher', 'language')

    # Makes it editable
    list_editable = ('is_published',)

    # Search functionality
    search_fields = ('code', 'title', 'author', 'medium', 'publisher', 'language')

# Register your models here.
admin.site.register(Livro, LibraryAdmin)

class ReservationAdmin(admin.ModelAdmin):
    # Show date in the admin page
    list_display = ('id', 'code', 'title', 'is_available', 'checkout_date', 'return_date', 'user_id')
    
    # Add links to items in the admin area
    list_display_links = ('id', 'code', 'title', 'user_id')

    # Creates a filter for the items below
    list_filter = ('code', 'title', 'user_id')

    # Makes it editable
    list_editable = ('is_available',)

    # Search functionality
    search_fields = ('code', 'title')

# Register your models here.
admin.site.register(Reserva, ReservationAdmin)