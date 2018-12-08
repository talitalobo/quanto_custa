from django.db import models

# Create your models here.

class Empresa(models.Model):
    razao_social=models.CharField(max_length=255)
    cnpj=models.CharField(max_length=25)
    informacoes_adicionais = models.TextField(null=True)

class Obra(models.Model):
    descricao = models.CharField(max_length=255,null=True)
    data_inicial = models.DateField(null=True)
    data_final = models.DateField(null=True)
    orcado = models.DecimalField(max_digits=128,decimal_places=2)
    informacoes_adicionais = models.TextField(null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True)
