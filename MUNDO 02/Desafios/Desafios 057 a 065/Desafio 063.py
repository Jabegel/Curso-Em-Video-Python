# 063 Escreva um programa que leia um número n interio qualquer e mostre na tela os n primeiros elementos de uma 
# Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
# F(n)=F(n−1)+F(n−2)

n = int(input('Escreva um número: '))
c = 3
f1 = 0
f2 = 1

print(' {} ➔  {}'.format(f1, f2), end = '')

while c <= n:
    f3 = f1 + f2
    print(' ➔  {}'.format(f3), end = '')
    f1 = f2
    f2 = f3
    c += 1
print(' ➔  FIM')