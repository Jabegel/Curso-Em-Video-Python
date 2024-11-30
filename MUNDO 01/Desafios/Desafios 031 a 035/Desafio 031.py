# 031 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distânca da Viagem?(Km) '))
if d <= 200:
    tc = 0.50
    vfc = d * tc
    print('O valor da passagem é R${}'.format(vfc))
else:
    tl = 0.45
    vfl = d * tl
    print('O valor da passagem é R${}'.format(vfl))