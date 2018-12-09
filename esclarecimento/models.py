from django.db import models
from obras.models import Obra
from django.contrib.auth.models import User
# Create your models here.

class Esclarecimento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(null=True)
    gps_lat = models.DecimalField(max_digits=9,decimal_places=6,null=True)
    gps_long = models.DecimalField(max_digits=9,decimal_places=6,null=True)
    data_criado = models.DateTimeField(auto_now_add=True)
    obra = models.ForeignKey(Obra,on_delete=models.PROTECT,null=True)
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    ABERTO = 1
    PROCESSANDO = 2
    FINALIZADO = 3
    status_choices = (
        (ABERTO, 'Não tem novidades'),
        (PROCESSANDO, 'Deram andamento'),
        (FINALIZADO, 'Finalizado'),
    )
    status = models.IntegerField(choices=status_choices,null=True)

    def get_foto_principal(self):
        dado = self.foto_esclarecimento_set.filter(principal=True).first()
        if dado is not None:
            dado = dado.foto
            return dado
        else:
            dado = None
            return False

    def status_css(self):

        if self.status==None:
            return "card abrt"
        if self.status == self.ABERTO:
            return "card abrt"
        if self.status == self.PROCESSANDO:
            return "card andt"
        if self.status == self.FINALIZADO:
            return "card fchd"


class Chat(models.Model):
    esclarecimento = models.ForeignKey(Esclarecimento,on_delete=models.PROTECT)
    mensagem=models.TextField(null=True)
    data_criado = models.DateTimeField(auto_now_add=True)
    autor=models.ForeignKey(User,on_delete=models.PROTECT)

class Foto(models.Model):
    foto = models.ImageField(upload_to='fotos/',null=True)
    data_criado = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.PROTECT)


class Foto_Esclarecimento(models.Model):
    esclarecimento = models.ForeignKey(Esclarecimento,on_delete=models.PROTECT)
    foto = models.ForeignKey(Foto,on_delete=models.PROTECT)
    principal = models.BooleanField(null=True)
