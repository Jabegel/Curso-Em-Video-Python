# Desenvolva um programa que leia as duas notas 
# de um aluno, calcule e mostre a sua média

N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Dimite a segunda nota: '))

print('A média entre {:.2f} e {:.2f} é {:.2f} .'.format(N1, N2, (N1 + N2)/2))