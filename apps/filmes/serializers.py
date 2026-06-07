from rest_framework import serializers
from .models import Filmes,Genero

class FilmesVisualizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['id','titulo','ano_de_lancamento','genero']
        
class FilmesVisualizeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['id','sinopse','duracao','titulo','ano_de_lancamento','equipe','genero','catalogo']        

class FilmesAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['sinopse','duracao','titulo','ano_de_lancamento','equipe','genero','catalogo']
        
class GeneroVisualizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['id','tipo','descricao','catalogo']     
        
class GeneroAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = ['tipo','descricao','catalogo']     