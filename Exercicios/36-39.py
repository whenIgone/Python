
# Desafio 036
print('-=' * 20)
print('''Preciso do valor da casa,
do salário do comprador 
e em quantos anos ele vai pagar.''')

casa = float(input('O valor da casa: '))
salário = float(input('Salário do comprador: '))
anos = int(input('Quantos anos para finalizar o pagamento: '))

# para calcular a prestação, será o valor da casa sobre a qtd. de meses que ele vai pagar
prestação = casa / (anos * 12)
mínimo = (salário * 30) / 100

print('Para pagar uma casa de R${:.2f} tendo R${:.2f} de salário, a prestação será de R${:.2f}'.format(casa, salário, prestação))
if prestação <= mínimo:
    print('Você pode comprar a casa !')
elif prestação > mínimo:
    print('Você não consegue comprar a casa')

# Desafio 037

n = int(input('Digite um número inteiro: '))
conversão = int(input('''Opções de conversão:
1 para binário 
2 para octal
3 para hexadecimal  
'''))

# Vai pegar da posição 2 em diante
if conversão == 1:
    print('Seu número na forma binária: {}'.format(bin(n)[2:]))
elif conversão == 2:
    print('Seu número na forma octal: {}'.format(oct(n)[2:]))
elif conversão == 3:
    print('Seu número na forma hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Escolha uma opção válida.')

# Desafio 038

v1 = int(input('1° valor inteiro: '))
v2 = int(input('2° valor inteiro: '))

if v1 > v2:
    print('O primeiro valor é maior que o segundo.')
elif v2 > v1:
    print('O segundo valor é maior que o primeiro')
elif v1 == v2:
    print('Os dois valores são iguais.')

# Desafio 039

nascimento = int(input('Sua idade: '))
sexo = str(input('Sexo(M/F): ')).upper().strip()
falta = 18 - nascimento
passou = falta * (-1)

if sexo == 'M':
    if nascimento < 18:
        print('Falta {} ano(s) para seu alistamento no serviço militar.'.format(falta))
    elif nascimento == 18:
        print('Chegou a hora de se alistar no serviço militar.')
    elif nascimento > 18:
        print('Já passou-se {} anos do seu tempo de alistamento.'.format(passou))
elif sexo == 'F':
    print('O alistamento não está disponível para mulheres.')