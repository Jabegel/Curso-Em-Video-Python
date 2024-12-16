# 057 Faça um porgrama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça 
# a digitação novamente até ter um valor correto.

sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nDigite seu sexo: [M ou F] ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite conforme o informado acima')
print('Obrigado por informar seu sexo')