# 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O Número 6.127 tem a parte inteira 6.

import math 

num = float(input('Digite um Número:'))
print('O Número {} tem a parte inteira {}.'.format(num,math.trunc(num)))
# math.floor // Arredonda para baixo
# math.trunc // Corta a parte inteira do número e mostra apenas el