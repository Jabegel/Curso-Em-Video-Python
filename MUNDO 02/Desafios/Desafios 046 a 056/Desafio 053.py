# 053 Crie um programa que leia uma frase qualquer e digas se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
# Separa e deixa tudo em Maiusculo
palavras = frase.split()
# Remove os espaços
junto = ''.join(palavras)
# Junta toda a lista
inverso = ''
# '' porque é uma string para dizer que ela está vazia para rodar no loop for
for letra in range(len(junto) -1, -1, -1):
    # Pego o tamanho da palavra já junta sem espaços e a Lê de trás para frente por conta do último -1
    inverso += junto[letra]
    # Aqui ajustar e monta as letras para forma inversa
if inverso == junto:
    # Confere se está igual ao digitado
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')