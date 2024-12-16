# 042 Refaça o DESAFIO 035 dos triângulos, acrescentando o recuso de mostrar que tipo de
# triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input('Diga o comprimento da primeira reta: '))
r2 = float(input('Diga o comprimento da segunda reta: '))
r3 = float(input('Diga o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um', end ='')
    if r1 == r2 == r3:
        print(' Triângulo Equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print(' Triângulo Isósceles')
    elif r1 != r2 != r3 != r1:
        print(' Triângulo Escaleno')
else:
    print('Os segementos acima NÃO PODEM FORMAR um Triângulo')