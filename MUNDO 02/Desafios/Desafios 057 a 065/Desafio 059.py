# 059 Crie um programa que leia dois valores e mostre um menu na tela:
# [1] soma
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
menu = 0
while menu != 5:
    print('\n1 - Soma')
    print('2 - Multiplicador')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair do Programa')
    menu = int(input('\nDigite sua ação: '))
    if menu == 1:
        print('\nVocê escolheu:')
        print('1 - Soma')
        print('A Soma de {} + {} = {}'.format(n1,n2,n1 + n2))
    elif menu == 2:
         print('\nVocê escolheu:')
         print('2 - Multiplicador')
         print('A Multiplicação de {} x {} = {}'.format(n1,n2,n1 * n2))
    elif menu == 3:
        print('\nVocê escolheu:')
        print('3 - Maior')
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif menu == 4:
        print('\nVocê escolheu:')
        print('4 - Novos números') 
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    else:
        print('OPÇÃO INVALIDA')


print('VOCÊ SAIU DO PROGRAMA')