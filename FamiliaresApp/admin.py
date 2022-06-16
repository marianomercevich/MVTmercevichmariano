from django.contrib import admin
from .models import Familiar

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'fecha_de_nacimento', 'edad', 'email', 'telefono')
admin.site.register(Familiar, FamiliarAdmin)