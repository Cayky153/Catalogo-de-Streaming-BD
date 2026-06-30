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
        return Response({"mensagem": "não implementado"})


# Tarefa: Adicionar Plano
class PlanosCreateView(generics.CreateAPIView):
    queryset = Planos.objects.all()
    serializer_class = PlanosAddSerializer  
