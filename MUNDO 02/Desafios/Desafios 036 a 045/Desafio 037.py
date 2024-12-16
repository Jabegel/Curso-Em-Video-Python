# 037 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será 
# a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Qual o número deseja converte? '))

print('Qual tipo de conversão deseja?')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')

e = input('Digite o número de 1 a 3: ')

if e == '1':
    print('Binario que é {}'.format(bin(n)))
elif e == '2':
    print('Octal que é {}'.format(oct(n)))
else:
    print('Hexadecimal que é {}'.format(hex(n)))