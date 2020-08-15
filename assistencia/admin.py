from django.contrib import admin
from .models import Assistencia

# Register your models here.
class AssistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'demmand', 'name', 'description')

    list_display_links = ('id', 'name')

    # Makes it editable
    list_editable = ('is_published',)

    search_fields = ('name', 'description')

# Make this show on the admin area
admin.site.register(Assistencia, AssistenciaAdmin)