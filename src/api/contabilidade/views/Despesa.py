from rest_framework import generics

from contabilidade.models.Despesa import Despesa
from contabilidade.serializer.Despesa import DespesaSerializer


class DespesaList(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer


class DespesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer