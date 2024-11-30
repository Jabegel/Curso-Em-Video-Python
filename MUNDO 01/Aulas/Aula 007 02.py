n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#.2f ou .nf é representa a quantidade de casas decimais que quero da divisão
#, end= '' serve para juntar um print com o outro, devem ser escrito no final do codigo

print('A soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(s,m,d))
print('A Divisão inteira é {} e a pontência é {}'.format(di,e))