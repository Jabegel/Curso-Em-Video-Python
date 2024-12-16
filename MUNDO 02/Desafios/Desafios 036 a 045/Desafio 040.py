# 040 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Qual a sua primeira nota?'))
n2 = float(input('Qual a sua segunda nota?'))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média está abaixo de 5.0.\nSua média é {:.1f}.'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua média está entre 5.0 e 6.9.\nSua média é {:.1f}.'.format(media))
else:
    print('Sua média está 7.0 ou superior.\nSua média é {:.1f}.\nPARABÉNS!'.format(media))