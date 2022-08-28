from urllib import request
from django.utils import timezone

from rest_framework import generics
from rest_framework.exceptions import ValidationError

from contabilidade.models.Receita import Receita
from contabilidade.serializer.Receita import ReceitaSerializer

class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

    def perform_create(self, serializer):
        description = serializer.validated_data.get('descricao').lower()
        current_month = timezone.now().month
        queryset = self.queryset.filter(
            descricao=description, create_at__month=current_month
        )
        if queryset:
            raise ValidationError('Erro: Receita já cadastrada para este mês!')
        else:
            serializer.save()

    def get_queryset(self):
        r = self.request.GET.get('descricao')
        if r:
            return Receita.objects.filter(descricao__icontains=r)
        return super().get_queryset()

class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
