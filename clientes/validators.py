import re
from validate_docbr import CPF



def nome_valido(nome):
    return str(nome).replace(' ', '').isalpha()
    
def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
