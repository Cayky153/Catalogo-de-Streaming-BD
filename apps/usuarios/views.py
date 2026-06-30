from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClientePlanoUpdateSerializer

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
    
    
class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response([])   

# Tarefa: Adicionar Cliente
class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Tarefa: Visualizar Assinatura
class AssinaturaDetailView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Tarefa: Atualizar Perfil de usuário
class UsuarioUpdateView(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  