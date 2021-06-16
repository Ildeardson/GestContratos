from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contratos(models.Model):
    tipo = models.CharField(verbose_name='Tipo', max_length=50)
    ident_contrato = models.CharField(verbose_name='Identiicação do contrato', max_length=50)


    class Meta:
        ordering = ['tipo']
        verbose_name_plural = 'Contratos'


    def __str__(self):
        return self.ident_contrato



