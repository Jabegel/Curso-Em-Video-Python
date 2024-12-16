# 067 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo.

while True:

    print('-' * 20)
    n = int(input('Digite um número: '))
    print('-' * 20)

    if n < 0:
        print('SAINDO DO PROGRAMA!')
        break

    print('-' * 20)
    print(f'TABUADA DO {n}')
    print('-' * 20)
    for c in range(0,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 20)