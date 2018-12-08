from .models import Esclarecimento,Foto,Foto_Esclarecimento
from django.contrib.auth.models import User

def get_reclamacao_post(request,id=None):
    mensagem_erro=None
    if id==None:
        esclarecimento=Esclarecimento()
    else:
        esclarecimento=Esclarecimento.objects.get(id=id)


    titulo=request.POST.get('titulo')
    descricao=request.POST.get('descricao')
    email = request.POST.get('email')
    gps_lat = request.POST.get('gps_lat')
    gps_long = request.POST.get('gps_long')

    email = email.lower()
    nickname=email.split("@")[0]+email.split("@")[1]

    autor,criado = User.objects.get_or_create(email=email,username=nickname)

    esclarecimento.autor=autor
    esclarecimento.titulo=titulo
    esclarecimento.descricao=descricao
    esclarecimento.gps_lat=gps_lat
    esclarecimento.gps_long=gps_long

    esclarecimento.save()

    # parte que ira tratar das Foto_Esclarecimento
    foto_placa = Foto()
    foto_obra = Foto()

    foto_obra.foto=request.FILES['foto_obra']
    foto_placa.foto=request.FILES['foto_placa']

    foto_obra.autor=autor
    foto_placa.autor=autor

    foto_obra.save()
    foto_placa.save()

    foto_vinculo=Foto_Esclarecimento()
    foto_vinculo.esclarecimento=esclarecimento
    foto_vinculo.foto=foto_obra
    foto_vinculo.principal=False
    foto_vinculo.save()

    foto_vinculo2=Foto_Esclarecimento()
    foto_vinculo2.esclarecimento=esclarecimento
    foto_vinculo2.foto=foto_placa
    foto_vinculo2.principal=True
    foto_vinculo2.save()

    return esclarecimento,mensagem_erro

def get_chat(request,esclarecimento):
    mensagem_erro=None
    chat = Chat()

    mensagem = request.POST.get('mensagem')
    # esclarecimento_id=request.POST.get('esclarecimento_id')
    if request.user.is_authenticated():
        chat.autor=request.user
    else:
        email = request.POST.get('email')
        email = email.lower()
        nickname=email.split("@")[0]+email.split("@")[1]
        autor,criado = User.objects.get_or_create(email=email,username=nickname)
        chat.autor=autor

    chat.esclarecimento=esclarecimento
    chat.mensagem=mensagem
    chat.save()

    return chat,mensagem_erro
