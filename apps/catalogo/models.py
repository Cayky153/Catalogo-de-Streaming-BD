from django.db import models

# Create your models here.
class Catalogo(models.Model):
    id=models.AutoField(primary_key=True)
    quantidade_de_filmes = models.IntegerField(blank=True, null=True)
    data_entrada = models.DateField(blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'

class Planos(models.Model):
    id=models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    duracao = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    numero_de_telas = models.IntegerField(blank=True, null=True)
    qualidade = models.CharField(max_length=50, blank=True, null=True)
    anuncios = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planos'
