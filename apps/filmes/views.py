from django.shortcuts import render

# Create your views here.
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FilmesAddSerializer


class FilmesViewSet(viewsets.ViewSet):

    def list(self, request):
               
        with connection.cursor() as cursor:
            cursor.execute("""
                           SELECT id,titulo,ano_de_lancamento,genero_id
                           FROM filmes
                           """)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
        resultado = [
        dict(zip(columns, row))
        for row in rows
        ]    

        return Response(resultado)
    
    def retrieve(self,request,pk=None):
        if pk is None:
            return Response({"erro": "ID obrigatório"}, status=400)
    
        with connection.cursor() as cursor:
            cursor.execute("""
                     SELECT *
                     FROM filmes
                        WHERE id = %s
                        """, [pk])

            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()

        if not row:
            return Response({"erro": "Filme não encontrado"}, status=404)

        resultado = dict(zip(columns, row))

        return Response(resultado)
    
    def create(self,request):
        serializer = FilmesAddSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=400
        )
    
        dados = serializer.validated_data
     
        with connection.cursor() as cursor:
            cursor.execute("""
                            INSERT INTO filmes(
                                  sinopse,
                                  duracao,
                                  titulo,
                                  ano_de_lancamento,
                                  equipe,
                                  genero_id,
                                  catalogo_id)
                            VALUES(
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s,
                                %s)
                            RETURNING id    
                            """, [
                                 dados["sinopse"],
                                dados["duracao"],
                                 dados["titulo"],
                                 dados["ano_de_lancamento"],
                                dados["equipe"],
                                 dados["genero"].id,
                                dados["catalogo"].id
                                 ])      
            filme_id = cursor.fetchone()[0]
                            
        return Response({"mensagem": "Filme inserido com sucesso",
                          "id": filme_id,
                          "titulo": dados["titulo"],
                          "sinopse": dados["sinopse"],
                          "duracao": dados["duracao"],
                          "ano_de_lancamento": dados["ano_de_lancamento"],
                          "equipe": dados["equipe"],
                         "genero": dados["genero"].id,
                         "catalogo": dados["catalogo"].id
                         }, status=201)        
                
    def destroy(self,request,pk=None):
        with connection.cursor() as cursor:
            cursor.execute("""
                           DELETE FROM filmes
                           WHERE id=%s
                           """,[pk])
        return Response({"Mensagem:Filme removido com sucesso"},status=204)         
    
class GenerosViewSet(viewsets.ViewSet):

    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                           SELECT id, tipo, descricao, catalogo_id
                           FROM genero
                           """)
            
            columns = [col[0] for col in cursor.description]
            
            rows = cursor.fetchall()
            
        resultado = [
            dict(zip(columns, row))
            for row in rows
        ]    

        return Response(resultado)    