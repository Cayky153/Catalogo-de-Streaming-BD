from django.db import models

# Create your models here.
class Filmes(models.Model):
    id=models.AutoField(primary_key=True)
    sinopse = models.CharField(max_length=255, blank=True, null=True)
    duracao = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    ano_de_lancamento = models.IntegerField(blank=True, null=True)
    equipe = models.CharField(max_length=255, blank=True, null=True)
    genero = models.ForeignKey('Genero', on_delete=models.SET_NULL, blank=True, null=True)
    catalogo = models.ForeignKey('catalogo.Catalogo', on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = False
        db_table = 'filmes'


class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    catalogo = models.ForeignKey('catalogo.Catalogo', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'

class ClienteFilme(models.Model):
    pk = models.CompositePrimaryKey('cliente_id', 'filme_id')
    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    filme = models.ForeignKey('Filmes', on_delete=models.CASCADE)
    historico = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_filme'