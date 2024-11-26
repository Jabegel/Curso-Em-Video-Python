# 015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
# a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km = float(input('Quantos Km foram percorridos com o carro? '))
Dia = float(input('Quantos dias foi alugado o carro? '))

Kmc = Km * 0.15
DiaC = Dia * 60
Total = Kmc + DiaC

print('O preço a se pagar pelos dias alugados são R${} e o preço pelo Km rodado é de R${} . No Total dá R${}'.format(DiaC,Kmc,Total))