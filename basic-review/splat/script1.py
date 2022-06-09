# primeira função do *
# Desempacotamento de listas de argumentos
def func(a, b, c):
    print(a + b)


values = [7, 3, 5]
func(*values)

# Se passar o * nos parametros da função, o * tera a função de fazer exatamente o contrário...
# ele irá definir que o parametro pode receber uma quantidade ilimitada de valores como argumento em forma de tupla
def func1(*values):
    print(values)


func1(1, 2, 3, 5, 6)

# O operador ** dentro de uma função faz exatamente o que somente um * faz, porém os parametros ficaram encapsulados em forma de
# dicionários
def func3(**kwargs):
    print(kwargs)


user_age = 2**5
func3(name="Eduardo", matheus=3)
