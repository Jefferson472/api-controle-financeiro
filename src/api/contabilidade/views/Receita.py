from rest_framework import viewsets, generics
from ..models.Receita import Receita
from ..serializer.Receita import ReceitaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
