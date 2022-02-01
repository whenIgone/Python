from random import randint
from time import sleep

# Desafio 044

print('=' * 10 + " RAPOSA'S STORE " + '=' * 10)
compras = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Sua opção: '))

if opção == 1:
    # 10% de desconto
    desconto = compras - (compras * 10 / 100)
    print('Sua compra de R${:.2f} recebeu um desconto de 10% e ficará R${:.2f}.'.format(compras, desconto))
elif opção == 2:
    # 5% de desconto
    desconto = compras - (compras * 5 / 100)
    print('Sua compra de R${:.2f} recebeu um desconto de 5% e ficará R${:.2f}.'.format(compras, desconto))
elif opção == 3:
    print('Sua compra de R${:.2f} não recebeu desconto.'.format(compras))
elif opção == 4:
    total = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    totalparc = total / parcelas

    print('Sua compra será parcelada em {}x de R${:.2f} \033[31mCOM 20% DE JUROS\033[m.'.format(parcelas, totalparc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, total))
else:
    print('\033[31mEscolha uma opção válida.\033[m')

# Desafio 045

jogo = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)

print('=' * 20)
print('Vamos jogar JOKENPÔ!')
print('=' * 20)
print('''[ 0 ] - Papel
[ 1 ] - Pedra
[ 2 ] - Tesoura''')
escolha = int(input('Qual é a sua escolha? '))
print('Vamos jogar!')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(0.9)
print('=' * 20)
print('O computador escolheu: {}'.format(jogo[computador]))

if computador == 0: # Papel
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('VOCÊ PERDEU')
    elif escolha == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # Pedra
    if escolha == 0:
        print('VOCÊ PERDEU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # Tesoura
    if escolha == 0:
        print('VOCÊ VENCEU!')
    elif escolha == 1:
        print('VOCÊ PERDEU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('Escolha uma opção válida')