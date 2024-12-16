# 058 Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora 
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

palpite = 0
acertou = False

while not acertou:
    c = random.choice(l)
    
    print('\n')
    print('-=-' * 22)
    print('Vamos jogar um Jogo, tente adivinhar o número que estou pensando.')
    print('-=-' * 22)
    
    palpite += 1
    
    u = int(input('Escolha um número entre 0 e 10: '))
    
    if u == c:
        acertou = True
        print('Processando...')
        time.sleep(1)
        print('Você Acertou!\nParabéns!')
        print('Você escolheu {}.'.format(u))
    else:
        print('Processando...')
        time.sleep(1)
        print('Errou! Tente novamente.')
        print('O número que pensei era {}.'.format(c))
        print('Você escolheu {}.'.format(u))
        print('Vamos tentar de novo.')

print('\nForam necessárias {} tentativas para ganhar do computador.'.format(palpite))