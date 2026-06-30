from rest_framework import serializers
from .models import Usuario, Cliente
from apps.catalogo.serializers import PlanosVisualizeSerializer  

class UsuarioVisualizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'ddd', 'numero']


class UsuarioAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'senha', 'ddd', 'numero']



UsuarioSerializer = UsuarioAddSerializer


class ClienteSerializer(serializers.ModelSerializer):
    plano_detalhes = PlanosVisualizeSerializer(source='planos', read_only=True)  

    class Meta:
        model = Cliente
        fields = ['id_usuario', 'forma_de_pagamento', 'planos', 'plano_detalhes']  


class ClientePlanoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['planos']  