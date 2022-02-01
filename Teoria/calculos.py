# Sucessor e Antecessor, Desafio 005
#num1 = int(input('Digite um número para ver seu sucessor e seu antecessor: '))
#print('Sucessor: {} \n Antecessor: {}'.format(num1 + 1, num1 - 1))

# Dobro, triplo e raiz quadrada, Desafio 006
#num2 = int(input('Digite um número: '))
#print('Seu dobro é {} \n Seu triplo é {} \n Sua raiz quadrada arredondada é {:.2f}'.format(num2 * 2, num2 * 3, num2 ** (1/2)))

# Média de um aluno, Desafio 007
#nota1 = float(input('Sua primeira nota: '))
#nota2 = float(input('Sua segunda nota: '))
#media = (nota1 + nota2) / 2
#print('Sua média resultou em: {:.1f}'.format(media))

# Conversão comprimento, Desafio 008
#metro = float(input('Digite seu comprimento em metros: '))
#print('Seu comprimento em centímetros: {:.0f}cm \n Seu comprimento em milímetros: {:.0f}mm'.format(metro * 100, metro * 1000))

# Tabuada, Desafio 009
tabuada = int(input('Digite um número para ver sua tabuada: '))
print('{} x 1 = {}'.format(tabuada, tabuada * 1))
print('{} x 2 = {}'.format(tabuada, tabuada * 2))
print('{} x 3 = {}'.format(tabuada, tabuada * 3))
print('{} x 4 = {}'.format(tabuada, tabuada * 4))
print('{} x 5 = {}'.format(tabuada, tabuada * 5))
print('{} x 6 = {}'.format(tabuada, tabuada * 6))
print('{} x 7 = {}'.format(tabuada, tabuada * 7))
print('{} x 8 = {}'.format(tabuada, tabuada * 8))
print('{} x 9 = {}'.format(tabuada, tabuada * 9))
print('{} x 10 = {}'.format(tabuada, tabuada * 10))

# Dólar, Desafio 010
dinheiro = float(input('Sua quantia de reais em dólares: '))
print('US${}'.format(dinheiro * 5.08))

# Parede de tinta, Desafio 011
print('2m² = 1 litro de tinta')
largura = float(input('Largura da parede(m): '))
altura = float(input('Altura da parede(m): '))
area = largura * altura
l = area / 2
print('A parede de dimensão \033[34m{}\033[m x \033[36m{}\033[m possui uma área de \033[32m{}m²\033[m \n Serão necessários: \033[36m{}\033[m litros de tinta para pintá-la'.format(largura, altura, area, l))

# Desconto, Desafio 012
preço = float(input('Qual é o preço do produto: R$'))
desconto = preço * 5 / 100
print('O produto com 5% de desconto fica\033[33m R${:.2f}\033[m'.format(preço - desconto))

# Reajuste salarial, Desafio 013
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario * 15 / 100
print('O salário com um aumento de 15% passa a ser:\033[1;31m R${:.2f}\033[m'.format(salario + novo))