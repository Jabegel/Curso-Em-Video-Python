# 073 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocador da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

brasileirão = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional',
               'São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama',
               'EC Vitória','Atlético-MG','Fluminense','Grêmio','Juventude ',
               'Bragantino','Athletico-PR','Criciuma','Atlético-GO','Cuiabá',)

print(f'Os 5 primeiros colocados são: {brasileirão[0:5]}')
print(f'Os 4 ultimos colocados são: {brasileirão[16:20]}')
print(f'Os time em ordem alfabética ficaria: {sorted(brasileirão)}')
if 'Chapecoense' not in brasileirão:
    print('A Chapecoense não está no Brasileirão')
else:
    print(f'A Chapecoense está na posição: {brasileirão.index("Chapecoense") + 1}')