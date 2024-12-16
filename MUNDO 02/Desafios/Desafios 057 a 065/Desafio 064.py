# 064 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).

n = 0
c = 0
soma = 0

while n != 999:
    n = int(input('Digite um número[999 para parar]: '))
    c += 1
    soma += n

print('\nVocê saiu do Programa')
print('Você digitou {} números.'.format(c-1))
print('No total a soma dos números que escreveu é: {}'.format(soma-999))