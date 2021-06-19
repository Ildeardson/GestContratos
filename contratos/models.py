from produtos.models import Produtos
from django.utils.translation import deactivate_all
from fornecedores.models import Fornecedores
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contratos(models.Model):
    
    TIPO_FORNECIMENTO = [
        ('F','FORNECEIMENTO'),
        ('S', 'SERVIÇOS'),
    ]

    fornecedor = models.ForeignKey(Fornecedores, verbose_name='Fornecedor', on_delete=models.RESTRICT)
    modalidade = models.CharField(verbose_name='Modalidade', max_length=50)
    n_contrato = models.CharField(verbose_name='Nº Contrato', max_length=50)
    data = models.DateField(verbose_name='Data', auto_now=False)
    inicio = models.DateField(verbose_name='Inicio', auto_now=False)
    fim = models.DateField(verbose_name='Fim', auto_now=False)
    tipo_forn =  models.CharField(verbose_name='Tipo Fornecimento', max_length=50, choices=TIPO_FORNECIMENTO)
    produto = models.ManyToManyField(Produtos, verbose_name='Produto', related_name='contratos')


    class Meta:
        ordering = ['modalidade']
        verbose_name_plural = 'Contratos'


    def __str__(self):
        return self.n_contrato



