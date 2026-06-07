from rest_framework import serializers
from .models import Planos,Catalogo
class CatalogoVisualizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields= ['id','quantidade_de_filmes','data_entrada','data_saida']


class PlanosVisualizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planos
        fields = ['id','nome','duracao','preco','numero_de_telas','qualidade','anuncios']
        
class PlanosAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planos
        fields = ['nome','duracao','preco','numero_de_telas','qualidade','anuncios']
                