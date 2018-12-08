import unidecode
def remover_acento(palavra):
    palavra = unidecode.unidecode(palavra)
    return palavra
