from django.utils import timezone

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from contabilidade.models.Receita import Receita
from contabilidade.serializer.Receita import ReceitaSerializer


class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

    def perform_create(self, serializer):
        description = serializer.validated_data.get('descricao')
        current_month = timezone.now().month
        queryset = self.queryset.filter(
            descricao=description, create_at__month=current_month
        )
        if queryset:
            raise ValidationError('Erro: Receita já cadastrada para este mês!')
        else:
            serializer.save()


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
