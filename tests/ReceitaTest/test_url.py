from django.test import TestCase
from django.urls import reverse, resolve

class ReceitaTestCaseUrl(TestCase):
    def test_urls(self):
        self.assertEqual(reverse('receitas'), '/api/v1/receitas')
        self.assertEqual(resolve('/api/v1/receitas').view_name, 'receitas')

    def test_urls_detail(self):
        self.assertEqual(reverse('detail', kwargs={'pk': 1}), '/api/v1/receitas/1' )
        self.assertEqual(resolve('/api/v1/receitas/1').view_name, 'detail')
    
    def test_urls_mes_ano(self):
        self.assertEqual(reverse('ano_mes', kwargs={'ano': 2022, 'mes': 8}),
            '/api/v1/receitas/2022/8' )
        self.assertEqual(resolve('/api/v1/receitas/2022/8').view_name, 'ano_mes')
