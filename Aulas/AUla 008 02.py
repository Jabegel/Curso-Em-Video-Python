from math import ceil,sqrt
# Ctrl + Espace = ver a lista de funções

num = int(input('Digite um número: '))
raiz = sqrt(num)
# Quando importa soment a função não precisa do '.biblioteca' apenas a função mesmo

print('A raiz de {} é igual a {}'.format(num,ceil(raiz)))
# ceil = arredonda para cima