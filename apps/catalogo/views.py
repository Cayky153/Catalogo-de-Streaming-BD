from django.db import connection
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Planos
from .serializers import CatalogoVisualizeSerializer, PlanosAddSerializer, PlanosVisualizeSerializer


class CatalogoViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM catalogo")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
        resultado = [dict(zip(columns, row)) for row in rows]
        return Response(resultado)


class PlanosViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([])

    def retrieve(self, request, pk=None):
        return Response({"mensagem": "não implementado"})

    def create(self, request):
        serializer= PlanosAddSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=400
            )
        
        dados = serializer.validated_data
        
        with connection.cursor() as cursor:
            cursor.execute( """
                            INSERT INTO planos(
                                    nome,
                                    duracao,
                                    preco,
                                    numero_de_telas,
                                    qualidade,
                                    anuncios)
                             VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s)
                            RETURNING id    
                            """,[
                                dados["nome"],
                                dados["duracao"],
                                dados["preco"],
                                dados["numero_de_telas"],
                                dados["qualidade"],
                                dados["anuncios"]
                            ])
            planos_id= cursor.fetchone()[0]
        return Response({"mensagem": "Plano inserido com sucesso!",
                          "id": planos_id,
                          "nome": dados["nome"],
                          "duracao": dados["duracao"],
                          "preco": dados["preco"],
                          "numero_de_telas": dados["numero_de_telas"],
                          "qualidade": dados["qualidade"],
                          "anuncios": dados["anuncios"]
                          }, status=201)                         


 
