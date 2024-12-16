# 071 Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

dinheiro = int(input('Qual o valor do saque? R$'))
notas50cont = 0
notas20cont = 0
notas10cont = 0
notas01cont = 0


if dinheiro >= 50:
    notas50cont = dinheiro // 50
    dinheiro = dinheiro % 50

if dinheiro >= 20:
    notas20cont = dinheiro // 20
    dinheiro = dinheiro % 20

if dinheiro >= 10:
    notas10cont = dinheiro // 10
    dinheiro = dinheiro % 10

if dinheiro >= 1:
    notas01cont = dinheiro // 1
    dinheiro = dinheiro % 1

if notas50cont > 0:
    print(f'No total você recebeu {notas50cont} notas de R$50')
if notas20cont > 0:
    print(f'No total você recebeu {notas20cont} notas de R$20')
if notas10cont > 0:
    print(f'No total você recebeu {notas10cont} notas de R$10')
if notas01cont > 0:
    print(f'No total você recebeu {notas01cont} notas de R$1')