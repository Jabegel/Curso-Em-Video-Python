# 069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos

maisde18 = 0
homem = 0
mulhermenor20 = 0
r = ''

while True:
    idade = int(input('\nDigite sua Idade: '))
    sexo = str(input('Digite seu Sexo: [M/F] ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('Digite um sexo informado')
        sexo = str(input('Digite seu Sexo: [M/F] ')).upper()
    
    if idade >= 18:
        maisde18 += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade <= 20:
        mulhermenor20 += 1
    
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('\nDESEJA CONTINUAR? [S/N]')).upper()
    if r == 'N':
        print('\nFECHANDO O PROGRAMA')
        break

print(f'{maisde18} São Maiores de 18 Anos.')
print(f'No total teve {homem} Homem Cadastrados.')
print(f'No total teve {mulhermenor20} Mulheres menos de 20 Anos Cadastrados.')