# 060 Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um número: '))
c = n
f = 1

print('Calculando {}! = '.format(n), end = ' ')
while c > 0:
    print('{}'.format(c), end = ' ')
    print('x' if c > 1 else ' = ', end = ' ')
    f *= c
    c -= 1

    
print('{}'.format(f))