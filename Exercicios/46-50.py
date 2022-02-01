from time import sleep

# Desafio 046
for anoNovo in range(10, 0, -1):
    print(anoNovo)
    # sleep(1)
print('FELIZ ANO NOVO !!!')

# Desafio 047
for pares in range(2, 51, 2):
    print(pares)
print('==' * 10)
# desafio 048
s = 0
# contador
cont = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        cont += 1
        s += impares
print('A soma de todos os {} valores divisíveis por 3 é {}'.format(cont, s))
print('==' * 10)

# Desafio 049
tabuada = int(input('Tabuada de qual número?: '))
for t in range(1, 11):
    print('{} x {} = \033[32m{}\033[m'.format(tabuada, t, tabuada * t))

# Desafio 050
b = 0
cont2 = 0
for n in range(0, 6):
    n1 = int(input('{}° número: '.format(n + 1)))
    if n1 % 2 == 0:
        cont2 += 1
        b += n1
print('A soma dos {} números pares é: {}'.format(cont2, b))




