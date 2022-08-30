from django.test import TestCase

from contabilidade.models.Despesa import Despesa


class DespesaTestCase(TestCase):
    def setUp(self):
        self.despesa = Despesa.objects.create(
            descricao="Despesa Teste",
            valor=10
        )

    def test_descricao(self):
        self.assertEqual(self.despesa.descricao, "Despesa Teste")

    def test_valor(self):
        self.assertEqual(self.despesa.valor, 10)
