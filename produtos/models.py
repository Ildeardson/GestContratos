from django.db import models

# Create your models here.
class Produtos(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=300)
    un = models.CharField(verbose_name='UN', max_length=5, default="")
    quantidade = models.IntegerField(verbose_name='quantidade')
    valor = models.DecimalField(verbose_name="V. Unitário", max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.descricao

    def v_total(self):
        return self.quantidade * self.valor

    class Meta:
        ordering = ['descricao']
        verbose_name_plural = "Produtos"
