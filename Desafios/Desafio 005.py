# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

N = int(input('Digite seu número: '))
ant = N - 1
suc = N + 1

print('O antecessor de {} é {} e o seu sucessor é {}.'.format(N, ant, suc))
