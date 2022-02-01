import random
import math
# from math import pow, floor

# bibliotecas não padrão
import emoji

print(math.floor(30.1234))
print(math.ceil(30.89283))
print(math.trunc(566.1324242440312312))
print(math.factorial(10))
print(int(math.pow(5, 4)))

num = float(input('Calcule a raiz quadrada de: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é: {}'.format(num, math.floor(raiz)))

# Biblioteca random
x = random.random()
y = random.randint(0, 20)
print(x, y)

# Biblioteca emojis
print(emoji.emojize('Emoji do mundo: :earth_americas:', use_aliases=True))

# Desafio 016
numero = float(input('Digite qualquer número: '))
print(math.trunc(numero))

# Desafio 017
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))
# hipot = math.sqrt((catop * catop) + (catad * catad))
# print('A hipotenusa vai medir: {:.2f}'.format(hipot))
print('A hipotenusa vai medir: {:.2f}'.format(math.hypot(catop, catad)))

# Desafio 018
# A função sin, cos, tan calcula em radianos, é necessário converter o valor
ang = float(input('Qual ângulo você deseja saber?: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {}° tem o TANGENTE de {:.2f}'.format(ang, tangente))