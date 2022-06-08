## Como declarar funções no python

def my_function():
    print("Hello from my function!") 

my_function()

## Passar argumentos
def my_function_with_args(username, greeting):
    print("Hello, %s , From my Function!, I wish you %s" % (username, greeting))
my_function_with_args("TESTE", "123")

## Função com returno
def sub_two_numbers(a,b):
    return a-b
print(sub_two_numbers(2,1))