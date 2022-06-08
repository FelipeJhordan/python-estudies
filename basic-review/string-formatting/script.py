# O operador % é usado para formatar uma string com variaveis encapsulados em uma tupla
from calendar import formatstring


name = "Jown"
print("Hello, %s" %name)
# Com dois ou mais argumentos
age = 21
surname = "Alves"
print("Hello, %s %s - %d years old" % (name, surname, age))

# Funciona com lista também
mylist = [1,2,3]
print("A list: %s" %mylist)

# Exemplo mais complexo

data = ("Jown", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.2f"
print(format_string % data)