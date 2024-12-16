# 061 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando estrutura while.

primeiro = int(input('Primeiro termo: '))
razão =int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
i = primeiro

while i <= décimo:
    print('{} '.format(i), end=' ➔  ')
    i += razão

print('ACABOU')