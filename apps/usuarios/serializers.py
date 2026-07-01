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


class ClienteSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Cliente
        fields = ['id_usuario', 'forma_de_pagamento', 'planos']  
        
        
class ClientePlanoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['planos']  