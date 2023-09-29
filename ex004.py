# Desafio 004 - Faça um programa que leia algo digitado e mostre todos os tipos primitivos.


lista = []

while True:
    nova_lista = input('Digite qualquer coisa: ')
    lista.append(nova_lista)
    parar = input('Se quiser parar de adicionar digite x: ')
    if parar == 'x':
        #lista.remove('x')
        break

print(type(lista))

