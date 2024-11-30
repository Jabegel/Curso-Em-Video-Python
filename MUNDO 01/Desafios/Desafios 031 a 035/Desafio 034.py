# 034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

s = int(input('Qual seu salário? '))
if s >= 1250:
    a1 = (s * 10 / 100)
    print('Seu salário é R${} e teve um aumento de 10%, ele será de R${}'.format(s,s+a1))
else:
    a2 = (s * 15 / 100)
    print('Seu salário é R${} e teve um aumento de 15%, ele será de R${}'.format(s,s+a2))