# Desafio 061
# an = a1 + (n - 1) * r
print('Gerador de PA')
print('=-=' * 5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1

while cont < 11:
    print('{} -> '.format(termo), end='')
    termo = termo + razão
    cont += 1
print('FIM')


