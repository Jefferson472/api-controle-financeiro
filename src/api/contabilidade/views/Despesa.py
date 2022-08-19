from rest_framework import viewsets, generics
from ..models.Despesa import Despesa
from ..serializer.Despesa import DespesaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
