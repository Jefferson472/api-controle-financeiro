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
            descricao__icontains=description, create_at__month=current_month
        )
        if queryset:
            raise ValidationError('Erro: Despesa já cadastrada para este mês!')
        else:
            serializer.save()

    def get_queryset(self):
        request = self.request.GET.get('descricao')
        if request:
            return Despesa.objects.filter(descricao__icontains=request)
        return super().get_queryset()


class DespesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer


class DespesaMes(generics.ListAPIView):
    serializer_class = DespesaSerializer

    def get_queryset(self):
        return Despesa.objects.filter(
            create_at__year=self.kwargs['ano'],
            create_at__month=self.kwargs['mes']
        )
