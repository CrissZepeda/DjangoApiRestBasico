from django.contrib import admin
from .models import Reservas

# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','fono', 'fecha', 'hora', 'cantidad','estado', 'observacion']
    
    
admin.site.register(Reservas, ReservasAdmin)