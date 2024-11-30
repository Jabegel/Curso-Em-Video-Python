# 025 Crie um programa que leia o nome de uma pesoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome: ')
print('Seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))