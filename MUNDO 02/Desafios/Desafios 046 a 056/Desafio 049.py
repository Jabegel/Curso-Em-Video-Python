# 049 Refaça o DESAFIO 009, mostrando a tabuada de número que o usuário escolher, só que agora utulizando 
# um laço for.

n = int(input('Escolha um número: '))

print('-=-' * 5)
print('TABUADA')
for c in range (0,11):
    print('{} x {} = {}'.format(n,c,n * c))
print('-=-' * 5)