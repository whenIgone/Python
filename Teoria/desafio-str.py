# Desafio 024
cidade = str(input('Digite o nome da sua cidade: ')).strip().capitalize()
# print(cidade[:5 == 'Santo'])
print(cidade.split(' ')[0] == 'Santo')

# Procurando uma string dentro de outra, Desafio 025
completo = str(input('Digite seu nome completo: ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in completo))

# Desafio 026
# rfind() / lfind()
frase = str(input('Digite qualquer frase: ')).strip().lower()
print('''Nesta frase, a letra "a" aparece {} vezes, 
aparecendo primeiro na posição {} e aparecendo pela última vez na posição {}
'''.format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))

# Primeiro e último nome de uma pessoa, Desafio 027
primeiroUltimo = str(input('Digite seu nome completo: ')).strip()
mudar = primeiroUltimo.split()
print('''Prazer em te conhecer !
Seu primeiro nome é: {}
Seu último nome é: {}
'''.format(mudar[0], mudar[len(mudar) - 1]))

