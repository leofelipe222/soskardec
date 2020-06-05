from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'message')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'message')

# Make this show on the admin area
admin.site.register(Contact, ContactAdmin)