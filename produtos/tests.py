from django.test import TestCase

# Create your tests here.
from .models import Produtos


class ProdtosModelTests(TestCase):

    def setUp(self):
        self.prod1 = Produtos()
        self.prod1.descricao = "arroz"
        self.prod1.un = 'un'
        self.prod1.quantidade = 10 
        self.prod1.valor = 50.00

    def test_fildes_models(self):
        self.assertEqual(self.prod1.descricao, "arroz")
        self.assertEqual(self.prod1.valor, 50.00)
        
    def test_funç_v_total(self):
        self.assertEqual(self.prod1.v_total(), 500.00)


