from django.test import TestCase
from django.urls import reverse, resolve

class DespesaTestCaseUrl(TestCase):
    def test_urls(self):
        self.assertEqual(reverse('despesas'), '/api/v1/despesas')
        self.assertEqual(resolve('/api/v1/despesas').view_name, 'despesas')

    def test_urls_detail(self):
        self.assertEqual(reverse('despesa_detail', kwargs={'pk': 1}), '/api/v1/despesas/1' )
        self.assertEqual(resolve('/api/v1/despesas/1').view_name, 'despesa_detail')
    
    def test_urls_mes_ano(self):
        self.assertEqual(reverse('despesa_ano_mes', kwargs={'ano': 2022, 'mes': 8}),
            '/api/v1/despesas/2022/8' )
        self.assertEqual(resolve('/api/v1/despesas/2022/8').view_name, 'despesa_ano_mes')
