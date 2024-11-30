nome = input('Qual o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

#:n é a quantidade de caracteres que irá usar para a string
print('\nPrazer em te conhecer {:20}!'.format(nome))


#:>n é a quantidade de caracteres que irá usar para a string porém alinhamento para direita
print('\nPrazer em te conhecer {:>20}!'.format(nome))


#:<n é a quantidade de caracteres que irá usar para a string porém alinhamento para esqueda
print('\nPrazer em te conhecer {:<20}!'.format(nome))

#:^n é a quantidade de caracteres que irá usar para a string porém alinhamento centralizado
print('\nPrazer em te conhecer {:^20}!'.format(nome))

#:=^n é a quantidade de caracteres que irá usar para a string porém alinhamento centralizado e com = centralizando
print('\nPrazer em te conhecer {:=^20}!'.format(nome))