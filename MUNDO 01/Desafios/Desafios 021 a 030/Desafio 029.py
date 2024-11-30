# 029 Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

v = float(input('Digite a velocidade em Km: '))

u = v - 80
m = u * 7

if v > 80:
    print('Você foi multado!')
    print('A multa será de R${}'.format(m))
else:
    print('Continue assim, seguindo a Lei!\nParabéns!')