import re


def nome_valido(nome):
        return nome.isalpha()
    
def cpf_valido(cpf):
    return len(cpf) == 11

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    '''Verifica se o celular é válido (11 91234-1234)'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
