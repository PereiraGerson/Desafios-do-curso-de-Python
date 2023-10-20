# Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores de 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter o valor correto.


sexo = str(input('Digite o sexo: [M]/[F]')).upper().strip()

while sexo not in 'MF':
       sexo =  str(input(('voce digitou errado, digite M ou F.'))).upper().strip()
print(input('sexo {} registrado com sucesso.'.format(sexo)))
