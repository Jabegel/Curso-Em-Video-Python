n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns, média Boa!')
else:
    print('Tem que estudar um pouco mais')