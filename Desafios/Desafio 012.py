# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

P = float(input('Qual o preço do Produto? '))
D = float(0.05)
VD = P * D
VF = P - VD

print('O Produto do valor de R${:.2f} tem o desconto de 5%, então seu valor no final será de: R${:.2f}'.format(P,VF))