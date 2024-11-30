# 014 Escreva um programa que converta uma temperatura digitando 
# em graus Celsius e converta para graus Fahrenheit.

# (0 °C × 9/5) + 32 = 32 °F

C = float(input('Qual o valor em Graus Celsius?'))
F = C * (9/5) + 32

print('{}ºC para Fahrenheit é {}ºF'.format(C,F))