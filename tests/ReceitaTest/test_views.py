from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from contabilidade.models.Receita import Receita


class ReceitaTestViews(APITestCase):
    def setUp(self):
        Receita.objects.create(
            descricao="Receita Teste",
            valor=10
        )

        self.user = User.objects.create(
            username="test_user", password="123456")
        self.client.login(username='test_user', password='123456')
        self.client.force_authenticate(user=self.user)

    def test_receita_list(self):
        res = self.client.get('/api/v1/receitas')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)
    
    def test_receita_detail(self):
        res = self.client.get('/api/v1/receitas/1')
        self.assertEqual(res.status_code, 200)

    def test_receita_update(self):
        res = self.client.put(
            '/api/v1/receitas/1',
            {
                'descricao': 'Receita Teste Atualizada',
                'valor': 11
            },
        )
        self.assertEqual(res.status_code, 200)
