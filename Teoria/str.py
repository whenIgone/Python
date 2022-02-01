texto = 'Curso em Vídeo Python'
letra = texto[9]
# Fatiamento
fatia = texto[9:]
# texto[::2] -> pulando de 2 em 2 sem saber o início ou fim
pular = texto[:21]
pular2 = texto[1:21:3]
pular3 = texto[11::2]
print(letra)
print(fatia)
print(pular)
print(pular2)

# Análise
# qts caracteres
print(len(texto))
# qts vezes aparece
print(texto.count('y'))
print('A letra "e" aparece {} vezes na frase'.format(texto.count('e', 0, 21)))
print(texto.find('Py')) # quando aparece
print('O' in texto) # tem no texto? True/False

# Transformação
print(texto.replace('Python', 'Javascript'))

print('O texto em maiúsculas fica: {}'.format(texto.upper()))
print('O texto em minúsculas fica: {}'.format(texto.lower()))

# Deixa só a primeira letra maiúscula
print('O texto em capitalize fica: {}'.format(texto.capitalize()))

# Deixa todas as primeiras letras maiúsculas
print('O texto em title fica: {}'.format(texto.title()))

#  strip()  /  rstrip()  / lstrip()    --> remove espaços desnecessários
fraseStrip = '                Testando o método strip           e   '
print(fraseStrip.strip())

# Divisão
# split(separator, maxsplit)
# print(texto.split(), fraseStrip.split())
dividir = texto.split()
print(dividir[3][4])

# Junção
print('-'.join(texto))

# Analisador de textos, Desafio 022
nome = str(input('Qual é seu nome Completo?: ')).strip()
primeiroNome = nome.split()[0]
print('''Seu nome todo maiúsculo fica: \033[4;36m{}\033[m
Seu nome todo minúsculo fica: \033[4;32m{}\033[m
Ao todo seu nome tem {} letras
Seu primeiro nome tem {} letras 
 '''.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(primeiroNome)))

# Separando dígitos de um número, Desafio 023
numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('''O número {} possui:
unidade: \033[1;34m {}\033[m
dezena: \033[1;35m {}\033[m
centena: \033[1;33m {}\033[m
milhar: \033[1;31m {}\033[m
'''.format(numero, u, d, c, m))

