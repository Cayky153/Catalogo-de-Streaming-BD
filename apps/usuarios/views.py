from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientePlanoUpdateSerializer

# === CLASSE QUE JÁ EXISTIA NO PROJETO ===
class ClienteViewSet(viewsets.ViewSet):
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
    