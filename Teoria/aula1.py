Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 8 + 1
9
>>> print("sexo inteligente")
sexo inteligente
>>> sexo = inteligente
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sexo = inteligente
NameError: name 'inteligente' is not defined
>>>  sexo = "inteligente"
 
SyntaxError: unexpected indent
>>> sexo = inteligente
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sexo = inteligente
NameError: name 'inteligente' is not defined
>>> sexo = "inteligente"
>>> sexo
'inteligente'
>>> print(sexo)
inteligente
>>> idade = 30
>>> idade
30
>>> print(sexo, idade)
inteligente 30
>>> sexo2 = input("O sexo é como?")
O sexo é como?
>>> sexo2
''
>>> sexo2 = input("O sexo é como?")
O sexo é como?inteligente
>>> sexo2
'inteligente'
>>> nome = input("Qual é seu nome?")
Qual é seu nome?Lucas
>>> nome
'Lucas'
>>> print("Olá" + nome " ! Prazer em te conhecer!")
SyntaxError: invalid syntax
>>> print("Olá" + nome +  "! Prazer em te conhecer!")
OláLucas! Prazer em te conhecer!
>>>  print("Olá " + nome +  "! Prazer em te conhecer!")
 
SyntaxError: unexpected indent
>>> print("Olá " + nome +  "! Prazer em te conhecer!")
Olá Lucas! Prazer em te conhecer!
>>> noe
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    noe
NameError: name 'noe' is not defined
>>> nome
'Lucas'
>>> oi = print("Olá " + nome +  "! Prazer em te conhecer!")
Olá Lucas! Prazer em te conhecer!
>>> oi
>>> Dia = input("Dia = ")
Dia = 30 
>>> Mes = input("Mes = ")
Mes = 12
>>> Ano = input("Ano = ")
Ano = 2003
>>> print("Você nasceu no dia" + Dia + "do mês " + Mes + "no ano de " + Ano)
