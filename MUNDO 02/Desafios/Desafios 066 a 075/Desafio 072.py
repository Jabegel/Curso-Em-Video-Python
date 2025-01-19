# 072 Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')

print('Escolha um número de 0 a 20')

while True:
    n = int(input('Qual número deseja ver? '))
    if n > 20:
        print('Número fora da lista')
    else:
        break
print(f'O número {n} por extenso é {extenso[n]}')