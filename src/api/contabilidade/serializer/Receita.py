from django.contrib import messages

from rest_framework import serializers

from ..models.Receita import Receita


class ReceitaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Receita
        fields = '__all__'
