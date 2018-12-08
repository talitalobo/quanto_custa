from .models import Obra,Empresa
from quanto_custa.utilidades import remover_acento

def get_empresa_post(request):
    razao_social = request.POST.get('razao_social')
    #ia usar para pesquisar pela razao social mas pode dar muito erro
    razao_social_sem_acento = remover_acento(razao_social)
    cnpj= request.POST.get('cnpj')
    informacoes_adicionais_empresa = request.POST.get("informacoes_adicionais_empresa")

    empresa = Empresa.objects.filter(cnpj=cnpj).first()

    if empresa is None:
        empresa = Empresa()
        empresa.razao_social=razao_social
        empresa.cnpj=cnpj
        empresa.informacoes_adicionais=informacoes_adicionais_empresa
        empresa.save()
    else:
        pass

    return empresa

def get_obra_post(request,id=None):
    if id==None:
        obra = Obra()
    else:
        obra = Obra.objects.get(id=id)

    descricao = request.POST.get('descricao')
    data_inicial = request.POST.get('data_inicial')
    data_final = request.POST.get('data_final')
    orcado = request.POST.get('orcamento')
    informacoes_adicionais = request.POST.get('informacoes_adicionais')
    empresa = get_empresa_post(request)

    obra.descricao=descricao
    obra.data_inicial=data_inicial
    obra.data_final=data_final
    obra.orcado=orcado
    obra.informacoes_adicionais=informacoes_adicionais
    obra.empresa=empresa

    obra.save()

    return obra
