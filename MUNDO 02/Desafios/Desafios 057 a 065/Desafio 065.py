# 065 Crie um programa que leia vários números interios pelo teclado. No final da execução, mostre a média entre 
# todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer 
# ou não continuar a digitar valores.

r = 'S'
n = 0
c = 0
soma = 0
maior = 0
menor = 0

while r == 'S':
    n = int(input('\nInforme um número: '))
    soma += n
    c += 1

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    r = str(input('Quer continuar? [S/N]')).upper()


print('FIM')
print('A média entre todos os valores é {}.'.format(soma/c))
print('O maior valor digitado foi: {}.'.format(maior))
print('O menor valor digitado foi: {}.'.format(menor))