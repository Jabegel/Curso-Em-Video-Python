# 041 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SENIOR
# Acima MASTER 

import datetime

ano_nascimento = int(input('Informe seu ano de Nascimento: '))

ano_atual = int(datetime.datetime.now().year)
idade = ano_atual - ano_nascimento

print('Sua idade é {} então você é um:'.format(idade))

if idade <= 9:
    print('Atleta Mirim')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade == 20:
    print('Atleta Senior')
else:
    print('Master')