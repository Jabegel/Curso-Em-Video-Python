# 028 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para 
# o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O Programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

l = [0,1,2,3,4,5]
c = random.choice(l)
print('-=-' * 22)
print('Vamos jogar um Jogo, tente a adivinha que número estou pensando.')
print('-=-' * 22)
u = int(input('Escolha um número entre 0 e 5: '))
if u == c:
    print('Processando...')
    time.sleep(1)
    print('Você Acertou!\nParabéns')
else:
    print('Processando...')
    time.sleep(1)
    print('Errou, boa sorte na próxima vez')
    print('O número que pensei era {}'.format(c))