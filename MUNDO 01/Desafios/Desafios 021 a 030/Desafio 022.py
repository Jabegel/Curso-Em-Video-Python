# 022 Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras Maiúsculas
# - O nome com todas a letras Minúsculas
# - Quantas letras ao todo(sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = input('Digite seu Nome Completo: ')

print(nome.upper())
print(nome.lower())
nome_d = nome.split()
print(len("".join(nome_d)))
print((len(nome_d[0])))