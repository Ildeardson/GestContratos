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
    cpf_cnpj = models.CharField(verbose_name='CNPJ/CPF', max_length=14)
    ie_forncedor = models.CharField(verbose_name='Incrição Estadual/RG', max_length= 20)
    endereco = models.CharField(verbose_name= 'Endereço', max_length=50)
    numero = models.CharField(verbose_name= 'Número', max_length= 6)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)
    cep = models.CharField(verbose_name='CEP', max_length=9)
    cidade = models.CharField(verbose_name='Cidade', max_length=50)
    UF = models.CharField(verbose_name='UF', max_length=2)
    telefone = models.CharField(verbose_name='Telfone', max_length=11)
    observações = models.TextField(verbose_name='Observações')

    
    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self) -> str:
        return self.razao_social

    
