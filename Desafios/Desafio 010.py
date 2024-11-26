# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere U$$ 1,00 = R$ 3,27

Di = float(input('Quanto dinheiro tem na carteira? R$'))
Do = Di / 3.27

print('Tendo R${:.2f} você poderá comprar U$${:.2f}'.format(Di,Do))