# 046 Faça um programa que mostre na ela uma contagem regressiva para o estouro, de fogos de artifício, 
# indo de 10 é 0, com uma pausa de 1 segundo entre eles.

import time

print('-=-' * 10)
print('A EXPLOSÃO OCORRERÁ EM:')

for c in range (10,0-1,-1):
    print(c)
    time.sleep(1)
if c == 0:
    print("BLOOMMMM")
print('-=-' * 10)