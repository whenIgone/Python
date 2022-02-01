from datetime import date
import time

# Ano Bissexto, Desafio 032
# Um ano é bissexto é um ano divisível por 4, exceto múltiplos de 100 que não são de 400
ano = int(input('Qual ano quer analisar? (Digite 0 para o ano atual em que está): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[32mbissexto.\033[m'.format(ano))
else:
    print('O ano {} NÃO é \033[32mbissexto.\033[m'.format(ano))


# maior e menor valor, Desafio 033
# dê o menor e maior valor para um aleatório, depois é só fazer a lógica com o resto
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print('O menor valor digitado foi \033[31m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[31m{}\033[m'.format(maior))

# Desafio 034
salario = float(input('Salário do funcionário (R$): '))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
elif salario <= 1250:
    salario = salario + (salario * 15 / 100)
print('O novo salário do funcionário é \033[34mR${:.2f}\033[m'.format(salario))

# Desafio 035
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a1 = float(input('Primeiro segmento: '))
a2 = float(input('Segundo segmento: '))
a3 = float(input('Terceiro segmento: '))
print('\033[1;33mANALISANDO...\033[m')
time.sleep(2)
if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    print('Os 3 segmentos \033[1;35mPODEM\033[m formar um triângulo.')
else:
    print('Os 3 segmentos \033[1;35mNÃO PODEM\033[m formar um triângulo')