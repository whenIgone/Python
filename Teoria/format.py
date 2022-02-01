n1 = int(input('digite um número: '))
n2 = float(input('digite um número: '))
soma = n1 + n2

print(type(n2))

# {} -> máscara trabalha com o .format
# print('A soma vale {}'.format(soma))

print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))

text = 'n'
print(text.isalpha())  # é letra?
number = input('Digite um número: ') # str
#print(number.isnumeric())
print(number.isalnum())