frase = 'Curso em Video Python'

print(len(frase))
# len retorna o comprimento de algo que está entre ()

print(frase.count('o'))
# variavel.count conta a quantidade de carecetes que você espeficou dentro do parenteses

print(frase.count('o', 0, 13))
# Quando colocamos x, y dentro do parenteses do count ele ira contar apenas dentro do paramentro informado

print(frase.find('deo'))
# variavel.find procura dentro da string os parametros que estão dentro do () e informa aonde ele começou

print(frase.find('Android'))
# Quando colocamos dentro do find uma string que não existe, ele retorna -1 que significa que não existe

print('Curso' in frase)
# 'String' in variavel retorna True ou False se tem a string dentro da variavel que colocamos