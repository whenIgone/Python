from datetime import date

# Desafio 051

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
# fórmula do enésimo termo
# quero o 10° termo
PA = primeiro + (10 - 1) * razao

for p in range(primeiro, PA + razao, razao):
    print('{}'.format(p))

# Desafio 052
total = 0
primo = int(input('Digite um número: '))
for f in range(1, primo + 1):
    if primo % f == 0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}\033[m'.format(f), end=' ')
print('\nO número {} foi divisível {} vezes,'.format(primo, total))
if total == 2:
    print('por isso, é NÚMERO PRIMO.')
else:
    print('Ele NÃO é um número primo.')
print('==' * 20)


# Palíndromo, Desafio 053
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
# print(frase.replace(' ', ''))
junto = ''.join(palavras)
inverso = ''
# uma opção de fatiamento: inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase: {} invertida é {},'.format(junto, inverso))
if junto == inverso:
    print('por isso é um palíndromo')
else:
    print('por isso NÃO é um palíndromo')


# Desafio 054
maior = 0
menor = 0
for d in range(0, 7):
    data = int(input('Ano de nascimento da {}° pessoa: '.format(d + 1)))
    analise = date.today().year - data
    if analise >= 21:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas, {} atingiram a maioridade,'.format(maior))
print('e {} ainda não atingiram a maioridade.'.format(menor))

# Desafio 055

big = 0
small = 0
# é a primeira ocorrência?
for n in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(n)))
    if n == 1:
        big = peso
        small = peso
    else:
        if peso > big:
          big = peso
        if peso < small:
            small = peso
print('O maior dos pesos lidos foi: {:.1f}kg'.format(big))
print('O menor dos pesos lidos foi: {:.1f}kg'.format(small))

# Desafio 056

somaIdade = 0
velhoIdade = 0
maioridadeHomem = 0
maioridadeMulher = 0
for info in range(1, 5):
    print('----- {}° PESSOA -----'.format(info))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if info == 1 and sexo in 'M':
        maioridadeHomem = idade
        velhoNome = nome
    if sexo in 'M' and idade > maioridadeHomem:
        maioridadeHomem = idade
        velhoNome = nome
    if sexo in 'F' and idade < 20:
        maioridadeMulher += 1


    somaIdade += idade

print('A média de idade do grupo é de {} anos,'.format(somaIdade / 4))
print('o homem mais velho tem {} anos e se chama {},'.format(maioridadeHomem, velhoNome))
print('há {} mulher(es) com menos de 20 anos.'.format(maioridadeMulher))


