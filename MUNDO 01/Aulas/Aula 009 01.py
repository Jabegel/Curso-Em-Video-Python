frase = 'Curso em Video Python'

print(frase[9])
# Quando colocamos uma variavel que contém uma string e colocamos variavel[x] podemos ver qual letra está na
# casa de x que colocamos

print(frase[9:14])
# Se colocarmos [x:y] sendo aonde tiver a letra x inicia a leitura e y finaliza com uma casa antes

print(frase[9:21])
# Se colocarmos no y uma casa que não tem na string, ele irá retornar até o final dela

print(frase[9:21:2])
# Se colocarmos um :z após delimitarmos o final da nossa string, ele ira pular a quantidade de casas de acordo com z

print(frase[:5])
# Se colocarmos :y estaremos pegando do inicio da string até o y

print(frase[15:])
# Se colocarmos x: estaremos pegando do x da string até o final dela

print(frase[9::3])
# Se colocarmos x::z iremos pegar x e ir indo até o final da string de z em z