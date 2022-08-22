from django.utils import timezone

from rest_framework import generics
from rest_framework.exceptions import ValidationError

from contabilidade.models.Despesa import Despesa
from contabilidade.serializer.Despesa import DespesaSerializer


class DespesaList(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

    def perform_create(self, serializer):
        description = serializer.validated_data.get('descricao').lower()
        current_month = timezone.now().month
        queryset = self.queryset.filter(
            descricao=description, create_at__month=current_month
        )
        if queryset:
            raise ValidationError('Erro: Despesa já cadastrada para este mês!')
        else:
            serializer.save()


class DespesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer