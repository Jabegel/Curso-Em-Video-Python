# Faça um programa que leia um ângulo qualquer
#  e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o seu ânguloº: '))
ang_rad = math.radians(ang)
seno = math.sin(ang_rad)
cose = math.cos(ang_rad)
tang = math.tan(ang_rad)

print('O Seno de {}º é {:.2f}'.format(ang,seno))
print('O Cosseno de {}º é {:.2f}'.format(ang,cose))
print('A Tangente de {}º é {:.2f}'.format(ang,tang))