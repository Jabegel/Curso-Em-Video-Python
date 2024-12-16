# 044  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o valor do Produto: R$'))
print('-=-' * 10)
print('1 - À vista dinheiro') #10% desconto
print('2 - À vista no cartão') #5% desconto
print('3 - Em até 2x no cartão') # preço normal
print('4 - 3x ou mais no cartão') #20% desconto
print('-=-' * 10)
e = input('\nQual a forma de pagamento?\n\nDigite o número de 1 a 4, para escolher: ')

desconto01 = float(produto / 10)
#10% 
desconto02 = float(produto / 20)
#5%
desconto03 = float(produto / 5)
#20%

if e == '1':
    print('O valor a ser pago é de R${:.1f}, com desconto de R${:.1f}'.format(produto - desconto01,desconto01))
elif e == '2':
    print('O valor a ser pago é de R${:.1f}, com desconto de R${:.1f}'.format(produto - desconto02,desconto02))
elif e == '3':
    print('O valor a ser pago é de R${:.1f}'.format(produto))
elif e == '4':
    print('O valor a ser pago é de R${:.1f}, com juros de R${:.1f}'.format(produto + desconto03,desconto03))