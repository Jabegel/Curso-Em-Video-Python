#Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo:')

print(type(a))
print('{} é tem letras ?'.format(a),a.isalpha())
print('{} é uma palavra toda em Maiuscula ?'.format(a),a.isupper())
print('{} é uma palavra toda em Minuscula ?'.format(a),a.islower())
print('{} é uma palavra com letras Maiusculas e Minusculas ?'.format(a),a.istitle())
print('{} é um Número ?'.format(a),a.isnumeric())
print('{} é um Número Decimal ?'.format(a),a.isdecimal())

