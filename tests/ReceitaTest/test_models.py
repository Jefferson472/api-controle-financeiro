from django.test import TestCase

from contabilidade.models.Receita import Receita


class ReceitaTestCase(TestCase):
    def setUp(self):
        self.receita = Receita.objects.create(
            descricao="Receita Teste",
            valor=10
        )

    def test_descricao(self):
        self.assertEqual(self.receita.descricao, "Receita Teste")

    def test_valor(self):
        self.assertEqual(self.receita.valor, 10)
