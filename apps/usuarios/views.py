from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientePlanoUpdateSerializer,ClienteSerializer,UsuarioAddSerializer

# === CLASSE QUE JÁ EXISTIA NO PROJETO ===
class ClienteViewSet(viewsets.ViewSet):
    def retrieve(self,request,pk=None):
        if pk is None:
            return Response({"erro": "ID obrigatório"}, status=400)
    
        with connection.cursor() as cursor:
            cursor.execute("""
                     SELECT c.id_usuario,p.nome,p.duracao,p.preco,p.numero_de_telas,p.qualidade,p.anuncios
                     FROM cliente AS c, planos AS p
                     WHERE c.id_usuario=%s AND c.planos_id=p.id
                        """, [pk])

            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()

        if not row:
            return Response({"erro": "Assinatura não encontrada"}, status=404)

        resultado = dict(zip(columns, row))

        return Response(resultado)
    
    def create(self,request):
        serializer = ClienteSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=400
        )
            
        dados= serializer.validated_data
        
        with connection.cursor() as cursor:
            cursor.execute("""
                            INSERT INTO cliente(
                                id_usuario,
                                forma_de_pagamento,
                                planos_id)
                            VALUES(
                                %s,
                                %s,
                                %s)
                        """,[dados["id_usuario"].id,
                             dados["forma_de_pagamento"],
                             dados["planos"].id
                             ])
        return Response({"Mensagem": "Cliente criado com sucesso",
                         "id_usuario": dados["id_usuario"].id,
                         "forma_de_pagamento": dados["forma_de_pagamento"],
                         "planos_id": dados["planos"].id})              
                                
   
    def update(self, request, pk=None):
        serializer = ClientePlanoUpdateSerializer(data=request.data)
        if not serializer.is_valid():
              return Response(
            serializer.errors,
            status=400
        )
        dados = serializer.validated_data
        with connection.cursor() as cursor:
            cursor.execute("""
                         UPDATE cliente
                         SET planos_id = %s
                         WHERE id_usuario = %s
                         """, [ dados["planos"].id, pk])
        return Response({"mensagem": "Plano de usuário atualizado"},status=200)
    ''
    
class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response([])   
    
    def create(self, request):
        serializer = UsuarioAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=400
            )
        dados = serializer.validated_data
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO usuario(
                    nome,
                    senha,
                    ddd,
                    numero)
                VALUES(
                    %s,
                    %s, 
                    %s, 
                    %s
                    )
                RETURNING id
            """, [
                dados["nome"],
                dados["senha"],
                dados["ddd"],
                dados["numero"]
            ])
            usuario_id = cursor.fetchone()[0]
        return Response(
            {
                "mensagem": "Usuario inserido com sucesso",
                "id": usuario_id,
                "nome": dados["nome"],
                "senha": dados["senha"],
                "ddd": dados["ddd"],
                "numero": dados["numero"]
            },
            status=201
        )
    
    def update(self, request, pk=None):

        serializer = UsuarioAddSerializer(data=request.data)

        if not serializer.is_valid():
              return Response(
            serializer.errors,
            status=400
        )
        dados = serializer.validated_data

        with connection.cursor() as cursor:
            cursor.execute("""
                         UPDATE usuario
                         SET nome= %s, senha = %s, ddd = %s, numero = %s
                         WHERE id = %s
                         """, [ dados["nome"],dados["senha"],dados["ddd"],dados["numero"], pk])

        return Response({"mensagem": "Usuario atualizado com sucesso"},status=200)
    

# === A NOSSA CLASSE COM AS DUAS TAREFAS ===
class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response([])

    # TAREFA: Visualizar perfil usuario
    def retrieve(self, request, pk=None):
        if pk is None:
            return Response({"erro": "ID obrigatório"}, status=400)

        with connection.cursor() as cursor:
            cursor.execute("""
                     SELECT id, nome, ddd, numero
                     FROM usuario
                     WHERE id = %s
                     """, [pk])
            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()

        if not row:
            return Response({"erro": "Usuário não encontrado"}, status=404)

        resultado = dict(zip(columns, row))
        return Response(resultado)

    # TAREFA: Remover usuário
    def destroy(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.execute("""
                           DELETE FROM usuario
                           WHERE id = %s
                           """, [pk])
            
        return Response({"mensagem": "Usuário removido com sucesso"}, status=204)
    
