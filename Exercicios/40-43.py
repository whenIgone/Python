import time
import datetime

nome = str(input('Qual é seu nome? ')).capitalize()

if nome == 'Lucas':
    print('Nome chave em pai slk')
elif nome == 'Miguel' or nome == 'Arthur' or nome == 'José':
    print('Todo mundo tem esse nome...')
elif nome in 'André Ana Amanda Alanis':
    print('Seu nome começa com A')

print('Bom dia {}.'.format(nome))

# Desafio 040

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
m = (nota1 + nota2) / 2

print('As notas {:.1f} e {:.1f} resultam na média {:.1f}'.format(nota1, nota2, m))

if m < 5:
    print('O aluno está REPROVADO.')
elif m >= 5 and m <= 6.9:
    # 5 <= m < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')

# Desafio 041

nas = int(input('Ano de nascimento do atleta: '))
anos = datetime.date.today().year - nas
print('Você tem {} anos.'.format(anos))
if anos <= 9:
    print('Sua categoria: MIRIM')
elif anos <= 14:
    print('Sua categoria: INFANTIL')
elif anos <= 19:
    print('Sua categoria: JÚNIOR')
elif anos <= 25:
    print('Sua categoria: SÊNIOR')
else:
    print('Sua categoria: MASTER')

# Desafio 042

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))
print('\033[1;33mANALISANDO...\033[m')
time.sleep(2)
if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    if a1 == a2 == a3:
        print('Os 3 segmentos \033[1;35mPODEM\033[m formar um triângulo \033[1;35mEQUILÁTERO\033[m.')
    elif a1 != a2 != a3 != a1:
        print('Os 3 segmentos \033[1;35mPODEM\033[m formar um triângulo \033[1;35mESCALENO\033[m.')
    else:
        print('Os 3 segmentos \033[1;35mPODEM\033[m formar um triângulo \033[1;35mISÓSCELES\033[m.')
else:
    print('Os 3 segmentos \033[1;35mNÃO PODEM\033[m formar um triângulo')


# Desafio 043

kg = float(input('Seu peso: (Kg) '))
altura = float(input('Sua altura: (m) '))
imc = kg / altura ** 2
print('O IMC dessa pessoa é: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de peso NORMAL')
elif imc >= 25 and imc < 30 :
    print('Você está na faixa de SOBREPESO')
elif imc >= 30  and imc < 40:
    print('Sinto muito, você está na faixa de OBESIDADE')
else:
    print('Sinto muito você está na faixa de OBESIDADE MÓRBIDA')

