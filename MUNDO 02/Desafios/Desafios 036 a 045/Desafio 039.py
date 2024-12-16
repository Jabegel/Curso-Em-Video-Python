# 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
# idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano_nascimento = int(input('Informe seu ano de Nascimento: '))

ano_atual = int(datetime.datetime.now().year)
idade = ano_atual - ano_nascimento
falta = 18 - idade
passou = idade - 18

if idade < 18:
    print('Você ainda vai se alistar, porque tem somente {} Anos.\nFalta ainda {} anos.'.format(idade,falta))
elif idade == '18':
    print('É a gora de se alistar, você já tem 18 Anos')
else:
    print('Já passou do tempo do alistamento.\nPassou {} anos'.format(passou))