from django.db import models
from quanto_custa.utilidades import remover_acento
# Create your models here.

class Empresa(models.Model):
    razao_social=models.CharField(max_length=255)
    razao_social_sem_acento=models.CharField(max_length=255,null=True)
    cnpj=models.CharField(max_length=25)
    informacoes_adicionais = models.TextField(null=True)

    def save(self,*args,**kwargs):
        self.razao_social_sem_acento = remover_acento(self.razao_social)
        super(Empresa, self).save(*args,**kwargs)

class Obra(models.Model):
    descricao = models.CharField(max_length=255,null=True)
    data_inicial = models.DateField(null=True)
    data_final = models.DateField(null=True)
    orcado = models.DecimalField(max_digits=128,decimal_places=2)
    informacoes_adicionais = models.TextField(null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT,null=True)
