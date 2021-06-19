from contratos.models import Contratos
from django.contrib import admin
from .models import Contratos

# Register your models here.

class ContratosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contratos, ContratosAdmin)