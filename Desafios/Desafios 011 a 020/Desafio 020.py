# 020 O mesmo professor do desafio anterios quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

nome1 = input('Digite o nome do Primeiro: ')
nome2 = input('Digite o nome do Segundo: ')
nome3 = input('Digite o nome do Terceiro: ')
nome4 = input('Digite o nome do Quarto: ')

lista = [nome1,nome2,nome3,nome4]

ordem = random.shuffle(lista)
# random.shuffle embaralha a ordem da lista que forneci

print('A ordem das apresentações será {}'.format(lista))