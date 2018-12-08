from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Esclarecimento,Chat
from .utilidades import get_reclamacao_post,get_chat
# Create your views here.
def index(request):
    template = loader.get_template("template_listando_tudo.html")
    context={}

    if request.method=="GET":

        esclarecimentos = Esclarecimento.objects.all()
        context.update(esclarecimentos=esclarecimentos)

        return HttpResponse(template.render(context,request))
    else:
        esclarecimento,mensagem_erro=get_reclamacao_post(request=request)
        context.update(esclarecimento=esclarecimento)

        chats = Chat.objects.filter(esclarecimento_id=esclarecimento.id).order_by('-id')
        context.update(chats=chats)

        template = loader.get_template("template_chat+obra.html")
        return HttpResponse(template.render(context,request))

def adicionar_chat(request,id):
    template = loader.get_template("template_chat+obra.html")
    context={}

    esclarecimento=Esclarecimento.objects.get(id=id)
    context.update(esclarecimento=esclarecimento)

    if request.method=="GET":
        pass

    else:
        chat,mensagem_erro = get_chat(request,esclarecimento)

    chats = Chat.objects.filter(esclarecimento_id=esclarecimento.id).order_by('-id')
    context.update(chats=chats)

    return HttpResponse(template.render(context,request))

    
