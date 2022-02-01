# nome = input("Qual é seu nome?")
# print('É um grande prazer te conhecer', nome)

# {:>x} {:^x} {:<x} {:=>x}
nome = input("Qual é seu nome? ")
print('É um grande prazer te conhecer {:=>20}!'.format(nome))


# {:.xf}
n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))
d = n1 / n2
# end='' / para não quebrar a linha
# \n  --> quebra de linha
print('A divisão desses \n dois fica: {:.1f}'.format(d), end=', ')
print('Potência: {}'.format(n1 ** n2))
