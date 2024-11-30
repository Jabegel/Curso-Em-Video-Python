# 026 Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = input('Digite sua frase: ').upper()
print('A Letra "A" aparece {} vezes'.format(frase.count('A')))
print('A posição que ela aparece pela primeira vez é {}'.format(frase.find('A')))
print('A posição que ela aparece pela ultima vez é {}'.format(frase.rfind('A')))