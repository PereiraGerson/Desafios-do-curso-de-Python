

def aumentar(preço, taxa):
    resultado = preço + taxa
    return resultado

def diminuir(preço, taxa):
    resultado = preço - taxa
    return resultado

def dobro(preço, taxa):
    resultado = preço / taxa
    return resultado

def metade(preço, taxa):
    resultado = preço / taxa
    return resultado

def moeda(valor):
    return f'R$ {valor:.2f}'
