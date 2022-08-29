from django.db.models import Sum
from django.http import JsonResponse

from contabilidade.models.Despesa import Despesa
from contabilidade.models.Receita import Receita


def ResumoList(request, **kwargs):
    ano = kwargs.get('ano')
    mes = kwargs.get('mes')
    context = {}
    context['categoria'] = {}

    receitas = Receita.objects.filter(create_at__year=ano, create_at__month=mes)
    context['receitas_valor_total'] = receitas.aggregate(Sum('valor'))

    despesas = Despesa.objects.filter(create_at__year=ano, create_at__month=mes)
    context['despesas_valor_total'] = despesas.aggregate(Sum('valor'))
    
    categoria = context['categoria']
    for despesa in despesas:
        if despesa.categoria in categoria:
            categoria[despesa.categoria] = categoria[despesa.categoria] + despesa.valor
        else:
            categoria[despesa.categoria] = despesa.valor

    context['saldo_final'] = context['receitas_valor_total']['valor__sum'] - \
        context['despesas_valor_total']['valor__sum']

    return JsonResponse(context, safe=False)
