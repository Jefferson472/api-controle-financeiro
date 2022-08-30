from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from contabilidade.models.Despesa import Despesa


class DespesaTestViews(APITestCase):
    def setUp(self):
        Despesa.objects.create(
            descricao="Despesa Teste",
            valor=10
        )

        self.user = User.objects.create(
            username="test_user", password="123456")
        self.client.login(username='test_user', password='123456')
        self.client.force_authenticate(user=self.user)

    def test_despesa_list(self):
        res = self.client.get('/api/v1/despesas')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)
    
    def test_despesa_detail(self):
        res = self.client.get('/api/v1/despesas/1')
        self.assertEqual(res.status_code, 200)

    def test_despesa_update(self):
        res = self.client.put(
            '/api/v1/despesas/1',
            {
                'descricao': 'Receita Teste Atualizada',
                'valor': 11
            },
        )
        self.assertEqual(res.status_code, 200)
