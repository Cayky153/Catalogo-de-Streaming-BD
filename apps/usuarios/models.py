
# Create your models here.
from django.db import models

class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    ddd = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'




class Cliente(models.Model):
    id_usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, db_column='id_usuario', primary_key=True)
    forma_de_pagamento = models.CharField(max_length=100, blank=True, null=True)
    planos = models.ForeignKey('catalogo.Planos', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cliente'




