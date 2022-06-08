# Em python não é necessário declarar tipos, tudo são objetos.

# Declarando Inteiros
myint = 1
print(myint)

# Declarando numeros flutuantes

myfloat = 7.3
print(myfloat)
myfloat = float(2)
print(myfloat)

# Strings são definidas com duas  aspas ou com aspas simples

mystring = "hello"
mystring2 = "world!"

print(mystring+" "+mystring2)

mystringwithapostrophes = "Don´t worry about 'apostrophes'"
print(mystringwithapostrophes)
mystringwithapostrophes = 'Don´t worry about "apostrophes"'
print(mystringwithapostrophes)

# Atruibuições podem ser feitas com mais de uma variavel ao mesmo tempo.
variavel1,variavel2 = 3,4
print(variavel1,variavel2)

# Operadores de mistura não são suportados entre
# numeros e letras no python ( não confundir com javascript)
one, two = 1,2
hello = "hello"
# print(one+two+hello)
# typeError: unsuported operand type(s)

# Exemplo de função nativa chamada isinstance (tipo instance of js)
myfloat = 10.0
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" %myfloat)
