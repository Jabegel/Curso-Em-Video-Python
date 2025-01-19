# 074 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerador e também indique o menor e o maior valor que estão na
# tupla.

import random

numeros = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
print(f'Os valores sorteados foram {numeros}')
print(f'O Maior valor sorteado foi {max(numeros)}')
print(f'O Menor valor sorteado foi {min(numeros)}')