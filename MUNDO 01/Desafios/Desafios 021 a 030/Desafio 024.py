# 024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

nome = input('Qual o nome da Cidade: ')
nome_d = nome.split()
print('SANTO' in nome_d[:5])