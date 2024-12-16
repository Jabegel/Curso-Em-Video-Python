# 056 Desevolva um programa que leia o nome, idade e sexo de 4 pessoas. No final o programa deve mostrar:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma = 0
homi_mais_velho = 0
nomevelho = ''
countmulher20 = 0

for p in range(0,4):
    nome = str(input('Digite seu nome: ')).upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M ou F): ')).upper()
    if sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo != 'f':
        print('Informe M para Masculino ou F para Feminino')
    print('\n')
    soma += idade

    if p == 1 and sexo == 'M':
        homi_mais_velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > homi_mais_velho:
        homi_mais_velho = idade
        nomevelho = nome
    
    if sexo == 'F' and idade < 20:
        countmulher20 += 1
    

print('A média de idade do grupo é de {}.'.format(soma/4))
print('O nome do Homem mais velho é {}'.format(nomevelho))
print('Ao todo são {} mulheres que tem menos de 20 Anos'.format(countmulher20))