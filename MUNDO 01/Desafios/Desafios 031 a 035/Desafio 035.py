# 035 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou 
# não formar um triângulo.

r1 = float(input('Diga o comprimento da primeira reta: '))
r2 = float(input('Diga o comprimento da segunda reta: '))
r3 = float(input('Diga o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um Triângulo')
else:
    print('Os segementos acima NÃO PODEM FORMAR um Triângulo')