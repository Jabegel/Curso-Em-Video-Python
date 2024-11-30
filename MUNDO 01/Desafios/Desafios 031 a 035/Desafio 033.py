# 033 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Qual o Primeiro Número: '))
n2 = int(input('Qual o Segundo Número: '))
n3 = int(input('Qual o Terceiro Número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O Maior valor digitado foi {}'.format(maior))
print('O Menor valor digitado foi {}'.format(menor))