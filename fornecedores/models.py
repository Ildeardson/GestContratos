from django.db import models
from django.db.models.fields import proxy

# Create your models here.
class Fornecedores(models.Model):
    TIPOS = [
        ('FISICA', 'FISICA'),
        ('JURIDICA', 'JURIDICA')
    ]
    tipo_forncedor = models.CharField(verbose_name='Tipor de Fornecedore', max_length=11, choices=TIPOS)
    razao_social = models.CharField(verbose_name='Razão Social', max_length=100,)
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=14)
    
    class Meta:
            verbose_name_plural = 'Fornecedores'
