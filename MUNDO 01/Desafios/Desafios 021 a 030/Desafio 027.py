# 027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro 
# e último nome separadamente.
# Ex. Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str((input('Digite seu nome Completo: '))).strip()
nome_s = nome.split()
print('O Primeiro Nome dele é: {}'.format(nome_s[0]))
print('O Último Nome dele é: {}'.format(nome_s[len(nome_s)-1]))