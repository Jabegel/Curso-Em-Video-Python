# 075 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tot9 = 0

tupla = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))


print(f'Você digitou os valores: {tupla}')
print(f'O número 9 aparecer {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)}ª posição')
else:
    print('O Valor 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram: ')
for n in tupla:
    if n % 2 == 0:
        print(n , end = ' ')