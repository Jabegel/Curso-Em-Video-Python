# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m^2
# A = b.h // A = l.a


l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))
Area = l * a
Q = Area / 2

print('A área da parede é de {:.2f} e a quantidade de tinta necessária para pintar será {:.2f}'.format(Area,Q))