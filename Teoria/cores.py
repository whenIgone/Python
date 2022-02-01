# Style : 0, 1, 4, 7
# Text : 30 à 37
# Background : 40 à 47

print('\033[0;30;41m inteligente \033[m')
print('\033[4;33;44m inteligente \033[m')
print('\033[1;36;45m inteligente \033[m')
print('\033[30;42m inteligente \033[m')
print('\033[30m inteligente \033[m')
print('\033[7m inteligente \033[m')

a = 3
b = 6
print('Os valores são \033[33m{}\033[m e \033[36m{}\033[m !'.format(a, b))

nome = 'Ruka'
print('Seu nome colorido: {}{}{}'.format('\033[1;32m', nome, '\033[m'))
#
cores = {'limpa': '\033[m',
         'roxo': '\033[1;35m',
         'azul': '\033[1;36m',
         'amarelo': '\033[1;33m'
         }
#
print('Seu nome colorido: {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))



