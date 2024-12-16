# 068 Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.

import random
import time

vitorias = 0

while True:
    print('\nESCOLHA P para PAR e I para IMPAR')
    escolhausuario = str(input('P ou I: ')).upper()
    escolhacomputador = ''
    if escolhausuario == 'P':
        print('Você escolheu PAR')
        escolhacomputador = 'I'
        print('O Computador escolheu IMPAR')
    else:
        print('Você escolheu IMPAR')
        escolhacomputador = 'P'
        print('O Computador escolheu PAR')
    
    time.sleep(0.5)
    print('\nUM')
    time.sleep(0.5)
    print('DO')
    time.sleep(0.5)
    print('LÁ')
    time.sleep(0.5)
    print('SI')
    time.sleep(0.5)
    print('E')
    time.sleep(0.5)
    print('JÁ!')

    computador = random.randint(0,10)
    usuario = int(input('\nDigite um número: '))
    soma = computador + usuario

    print(f'\nO computador escolheu {computador} e você escolheu {usuario}.\n{computador} + {usuario} = {soma}')
    if soma % 2 == 0:
        print('Então o total deu PAR')
    else:
        print('Então o total deu IMPAR')

    if soma % 2 == 0 and escolhausuario == 'P' and escolhacomputador == 'I':
        print(f'\nParabéns! Você ganhou escolhendo PAR a soma deu {soma}!')
        vitorias += 1
    elif soma % 2 == 1 and escolhausuario == 'I' and escolhacomputador == 'P':
        print(f'\nParabéns! Você ganhou escolhendo IMPAR a soma deu {soma}!')
        vitorias += 1
    else:
        print('\nVOCÊ PERDEU')
        break

print(f'\nVocê ganhou {vitorias} vezes consecutivas.')