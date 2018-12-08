from .models import Esclarecimento

def get_obra_post(request,id=None):
    if id==None:
        obra = Obra()
    else:
        obra = Obra.objects.get(id=id)

def get_reclamacao_post(request,id=None):
    if id==None:
        esclarecimento=Esclarecimento()
    else:
        esclarecimento=Esclarecimento.objects.get(id=id)


    titulo=request.POST.get('titulo')
    descricao=request.POST.get('descricao')
    
