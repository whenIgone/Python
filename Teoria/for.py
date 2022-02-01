
# laço c no intervalo(1, 10):
# for c in range(1, 10):
# estruturas condicionais nos laços de repetição

for x in range(0, 10):
    print(x)
print('FIM')

# o terceiro parâmetro define como será a contagem
# -1 faz a contagem inversa

for y in range(100, 0, -1):
    print(y)
print('FIM 2')

for z in range(0, 10, 2):
    print(z)
print('FIM 3')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Pulando de: '))
for a in range(inicio, fim + 1, passo):
    print(a)

for pergunta in range(0, 3):
    ask = int(input('Um número: '))
print('Fim 4')

# acumulando valores
s = 0
for t in range(0, 4):
    u = int(input('Um número inteiro: '))
    s += u
print('A soma de todos os números é {}'.format(s))

