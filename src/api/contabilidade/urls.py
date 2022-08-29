from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from contabilidade.views.Despesa import DespesaList, DespesaDetail, DespesaMes
from contabilidade.views.Receita import ReceitaList, ReceitaDetail, ReceitaMes
from contabilidade.views.Resumo import ResumoList


urlpatterns = [
    # Receitas
    path('api/v1/receitas', ReceitaList.as_view()),
    path('api/v1/receitas/<int:pk>', ReceitaDetail.as_view()),
    path('api/v1/receitas/<int:ano>/<int:mes>', ReceitaMes.as_view()),
    
    # Despesas
    path('api/v1/despesas', DespesaList.as_view()),
    path('api/v1/despesas/<int:pk>', DespesaDetail.as_view()),
    path('api/v1/despesas/<int:ano>/<int:mes>', DespesaMes.as_view()),

    # Resumo
    path('api/v1/resumo/<int:ano>/<int:mes>', ResumoList),
]

urlpatterns = format_suffix_patterns(urlpatterns)
