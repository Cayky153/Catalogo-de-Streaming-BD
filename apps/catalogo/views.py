from django.shortcuts import render

# Create your views here.
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CatalogoVisualizeSerializer

class CatalogoViewSet(viewsets.ViewSet):

    def list(self, request):
        serializer = CatalogoVisualizeSerializer
        
        
        with connection.cursor() as cursor:
            cursor.execute("""
                           SELECT * 
                           FROM catalogo
                           """)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
        resultado = [
        dict(zip(columns, row))
        for row in rows
        ]    

        return Response(resultado)
    
class PlanosViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response([])

    def retrieve(self, request, pk=None):
        return Response({"mensagem": "não implementado"})

    def create(self, request):
        return Response({"mensagem": "não implementado"})
