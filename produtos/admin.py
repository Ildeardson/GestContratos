from django.contrib import admin
from .models import Produtos

# Register your models here.

class ProdutosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Produtos, ProdutosAdmin)