from rest_framework import serializers
from .models import Entrada


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Entrada
        fields=['id', 'title', 'content', 'imagen']