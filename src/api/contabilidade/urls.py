from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from contabilidade.views.Receita import ReceitaList, ReceitaDetail
from contabilidade.views.Despesa import DespesaList, DespesaDetail


urlpatterns = [
    # Receitas
    path('api/v1/receitas/', ReceitaList.as_view()),
    path('api/v1/receitas/<int:pk>', ReceitaDetail.as_view()),
    
    # Despesas
    path('api/v1/despesas/', DespesaList.as_view()),
    path('api/v1/despesas/<int:pk>', DespesaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
