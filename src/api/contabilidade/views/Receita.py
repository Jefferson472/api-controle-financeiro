from rest_framework import generics

from contabilidade.models.Receita import Receita
from contabilidade.serializer.Receita import ReceitaSerializer


class ReceitaList(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class ReceitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
