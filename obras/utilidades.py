from .models import Obra

def get_obra_post(request,id=None):
    if id==None:
        obra = Obra()
    else:
        obra = Obra.objects.get(id=id)

    
