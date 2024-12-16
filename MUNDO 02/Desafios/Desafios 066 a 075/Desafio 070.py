# 070 Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário 
# vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato

soma = 0
maisde1000 = 0
nomemaisbarato = ''
maisbarato = -1
c = 1

while True:
    nome = str(input('\nDigite o Nome do Produto: '))
    preco = float(input('Digite o preço: R$ '))
    
    soma += preco

    if preco >= 1000:
        maisde1000 += 1
    
    if maisbarato == -1:
        maisbarato = preco
        nomemaisbarato = nome
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomemaisbarato = nome

    saida = str(input('DESEJA CONTINUAR? [S/N]')).upper()
    if saida == 'N':
        print('\nFECHANDO O PROGRAMA')
        break

print(f'No total deu R${soma}.')
print(f'No total teve {maisde1000} Produtos acima de R$1.000.')
print(f'O nome do Produto mais barato é {nomemaisbarato}.')