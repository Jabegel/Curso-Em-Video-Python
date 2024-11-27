# 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

nome1 = input('Digite o nome do Primeiro: ')
nome2 = input('Digite o nome do Segundo: ')
nome3 = input('Digite o nome do Terceiro: ')
nome4 = input('Digite o nome do Quarto: ')

lista = [nome1,nome2,nome3,nome4]
# Lista contém varios valores dentro de si // parecido com vetor

escolhido = random.choice(lista)
# random.choice escolhe algo de dentro de uma lista

print('O Aluno escolhido é {}'.format(escolhido))