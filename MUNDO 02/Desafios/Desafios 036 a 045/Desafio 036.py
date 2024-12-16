# 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
# será negado.

valor_da_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = float(input('Em quantos anos vai pagar? '))

meses = anos * 12
parcelas = valor_da_casa / meses
prestacao_porcentagem = parcelas * 100 / salario
prestacao_limite_porcentagem = 30
prestacao_limite_valor = salario * 30 / 100

if prestacao_porcentagem <= prestacao_limite_porcentagem:
    print('PARABÉNS SEU EMPRÉSTIMO FOI ACEITO')
    print('Você terá parcelas de R${:.2f} que é {:.2f} do seu salário'.format(parcelas,prestacao_porcentagem))
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('\nEMPRÉSTIMO NEGADO!')
    print('Nessas condições as parcelas serão 30%, ou mais do seu salário')
    print('Para não ficar sem o empréstimo você pode:')
    print('- Aumentar sua renda.')
    print('- Aumentar os anos que irá pagar.')
    print('- Diminuir o valor do empréstimo.')