# 045 Crie um programa que faça o computador jogar Jokenpô com você.
# Pedra > Tesoura = Pedra Ganha de Tesoura
# Pedra < Papel = Pedra Perde de Papel
# Tesoura > Papel = Tesoura Ganha de Papel
# Tesoura < Pedra = Tesousa Perde de Pedra
# Papel > Pedra = Papel Ganha de Pedra
# Papel < Tesoura = Papel Perde de Tesora

import random

print('-=-' * 5)
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('-=-' * 5)

pc = random.choice([1,2,3])

e = int(input('\nDigite sua escolha: '))

if e == 1:
    print('\nVocê escolheu:\n1 - Pedra')
elif e == 2:
    print('\nVocê escolheu:\n2 - Papel')
elif e == 3:
    print('\nVocê escolheu:\n3 - Tesoura')

if pc == 1:
    print('\nO Computador escolheu:\n1 - Pedra')
elif pc == 2:
    print('\nO Computador escolheu:\n2 - Papel')
elif pc == 3:
    print('\nO Computador escolheu:\n3 - Tesoura')

if e == 1 and pc == 3:
    print('\nPEDRA GANHA DE TESOURA!\nVocê ganhou!\nParabéns!\n')
elif e == 1 and pc == 2:
    print('\nPEDRA PERDE PARA PAPEL!\nVocê perdeu!\nMais sorte na próxima!\n')
elif e == 1 and pc == 1:
    print('\nEMPATE!\nNINGUÉM GANHOU!\nTENTE DE NOVO!\n')
elif e == 2 and pc == 1:
    print('\nPAPEL GANHA DE PEDRA!\nVocê ganhou!\nParabéns!\n')
elif e == 2 and pc == 3:
    print('\nPAPEL PERDE PARA TESOURA!\nVocê perdeu!\nMais sorte na próxima!\n')
elif e == 2 and pc == 2:
    print('\nEMPATE!\nNINGUÉM GANHOU!\nTENTE DE NOVO!\n')
elif e == 3 and pc == 1:
    print('\nTESOURA PERDE PARA PEDRA!\nVocê perdeu!\nMais sorte na próxima!\n')
elif e == 3 and pc == 2:
    print('\nTESOURA GANHA DE PAPEL!\nVocê ganhou!\nParabéns!\n')
elif e == 3 and pc == 3:
    print('\nEMPATE!\nNINGUÉM GANHOU!\nTENTE DE NOVO!\n')