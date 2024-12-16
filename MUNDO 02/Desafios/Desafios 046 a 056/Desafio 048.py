# 048 Faça um programa que calcule a soma entre todos os número impares que são múltiplos de três e
# que se encontram no intervalo de 1 ate 500.

soma = 0

for c in range (1,501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c

print('A soma dos números multiplos de 3 e impares é {}.'.format(soma))