
# Desafio 057, Validação de dados

sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]

while sexo not in "MF":
    print('Dados inválidos. Por favor,', end='')
    sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))

# Desafio 058

from random import randint

print('=' * 20)
print('Vamos brincar de adivinhação!')
print('Eu escolhi um número entre 0 e 10, qual será que é?')
num = int(input('Seu palpite: '))
computador = randint(0, 10)
acertou = False
tentativas = 1
while num != computador:
    acertou = acertou
    tentativas += 1
    if num > computador:
        print('Um pouco menos')
    elif num < computador:
        print('Um pouco mais')
    num = int(input('Seu palpite: '))

print('Meus parabéns, eu realmente escolhi o número {} '.format(computador))
print('Você acertou em {} tentativa(s)'.format(tentativas))
'''
while num != computador:
    if num > computador:
        print('Um pouco menos')
        num = int(input('Seu palpite: '))
    elif num < computador:
        print('Um pouco mais')
        num = int(input('Seu palpite: '))
    elif num > 10:
        print('Opção inválida, tente novamente.')
        num = int(input('Seu palpite: '))
print('Meus parabéns, eu realmente escolhi o número {} '.format(computador))
'''

# Desafio 059, Criando um menu de opções

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
soma = numero1 + numero2
multip = numero1 * numero2
opção = 0

while opção != 5:
    print('=-=' * 10)
    print('''Escolha uma operação para os dois números escolhidos:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opção = int(input('Opção escolhida: '))
    if opção == 1:
        print('{} + {} = {}'.format(numero1, numero2, soma))
    elif opção == 2:
        print('{} x {} = {}'.format(numero1, numero2, multip))
    elif opção == 3:
        if numero1 > numero2:
            print('O número {} é maior'.format(numero1))
        elif numero1 < numero2:
            print('O número {} é maior'.format(numero2))
        else:
            print('Os números são iguais')
    elif opção == 4:
        print('Informe os números novamente: ')
        numero1 = int(input('Primeiro número: '))
        numero2 = int(input('Segundo número: '))
        soma = numero1 + numero2
        multip = numero1 * numero2
    else:
        print('Opção inválida, escolha uma opção válida.')
print('Encerrando programa...')

# Desafio 060, Cálculo de fatorial

n = int(input('Digite um número para descobrir seu fatorial: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c != 1:
    print('{} x '.format(c), end='')
    # print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{} = {}'.format(c, f))

''' Usando o for
for c in range(c, f, -1):
    f *= c
    c -= 1
print(f)
'''







