# Escreva um programa que leia um valor em metros e o exiba convertido em centímentos e milímetros

M = float(input('Digite o valor em Metros: '))
Km = M / 1000
Hm = M / 100
Dam = M / 10
Dm = M * 10
Cm = M * 100
Mm = M * 1000

print('A medida de {}m corresponde a'.format(M))
print('{} Km '.format(Km))
print('{} Hm '.format(Hm))
print('{} Dam '.format(Dam))
print('{} Dm '.format(Dm))
print('{} Cm '.format(Cm))
print('{} Mm '.format(Mm))