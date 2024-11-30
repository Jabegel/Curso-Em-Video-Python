# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

S = float(input('Qual o seu salário? '))
A = float(0.15)
VA = S * A
VF = S + VA

print('O seu salário de R${:.2f} terá o aumento de 15%, então seu novo valor será de: R${:.2f}, teve uma aumento de R${:.2f}'.format(S,VF,VA))