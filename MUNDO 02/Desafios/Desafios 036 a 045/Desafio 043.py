# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
# seu status, de acordo com o a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# -  Acima de 40: Obesidade mórbida

peso = float(input('Qual o seu peso?(KG) '))
altura = float(input('Qual a sua altura? '))

icm = peso / (altura * altura)

print('Seu ICM é {:.1f}'.format(icm))
if icm < 18.4:
    print('Abaixo do Peso')
elif 18.5 <= icm < 25.0:
    print('Peso ideal')
elif 25.0 <= icm < 30.0:
    print('Sobrepeso')
elif 30.0 <= icm < 40.0:
    print('Obesidade')
else:
    print('Obesidade mórbida')