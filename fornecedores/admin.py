from django.contrib import admin
from .models import Fornecedores

# Register your models here.
class FornecedorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fornecedores, FornecedorAdmin)