# 017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

cat = float(input('Qual o valor do Cateto? '))
cato = float(input('Qual o valor do Cateto Oposto? '))

h = math.sqrt(math.pow(cat,2)+math.pow(cato,2))
# o math.pow necessida ter ',x' que é informando a que número estará sendo elevado

hipotenusa = math.hypot(cat,cato)
# math.hypot calcula hipotenusa automaticamente

print('O valor da Hipotenusa é {:.2f}'.format(h))
print('O valor da Hipotenusa é {:.2f}'.format(hipotenusa))