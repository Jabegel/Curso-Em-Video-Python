# 050 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o

soma = 0

for c in range (0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n 
    else:
        print('\nNúmero Impar, não será adicionado a soma\n')

print('A soma dos valores são {}'.format(soma))