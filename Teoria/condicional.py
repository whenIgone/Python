# Condições
# if / else

import random
import time

nome = str(input('Seu nome: ')).strip()
if nome[0] == 'L':
    print('RESENHA NÉ PAAIII')
else:
    print('Seu nome é meio paia sla')

n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Parabéns !')
else:
    print('Reprovado...')

# Desafio 028

aleatorio = random.randint(0, 5)
print('\033[35m-=-\033[m' * 20)
print('\033[1;33mTente descobrir o número que eu pensei entre 0 e 5\033[m')
print('\033[35m-=-\033[m' * 20)
resposta = int(input('Sua resposta: '))
print('\033[35mPROCESSANDO...\033[m')
time.sleep(2)
if aleatorio == resposta:
    print('\033[36mParabéns você acertou !!!\033[m')
else:
    print('\033[31mTente novamente.\033[m')

# Desafio 029

velocidade = float(input('Velocidade do seu carro em km/h: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('''Você foi multado.
A multa irá custar R$7,00 por cada km 
acima do limite''')
    print('''Com o carro à {:.1f}km/h,
você pagará R${:.2f} de multa'''.format(velocidade, multa))

