x = 2
print(x == 2 ) # True
print(x == 3 ) # False

## No python é utilizando o And para && e Or para || 
name = "Felipe"
age = 21
if name == "Felipe" and age == 21:
    print("Your name is Felipe, and you are also 23 years old.")
if name == "Maria" or name == "Rick":
    print("Your name is either Maria or Rick")

# Operador In para verificar se tal objeto existe dentro de um objeto container/lista

name = "Rock"
if name in ["Lee", "Rock"]:
    print("Your name is either Rock or Lee")

## Continue == pass


## Exemplo de se, senão se e senão
statment = False
another_statment = True
if statment is True:
    # Do something
    pass
elif another_statment is True:
    # Do something else
    pass
else:
    # Do another thing 
    pass

## Operador Is é utilizado para verificar a REFÊRENCIA das variaveis
x = [1,2,3]
y = [1,2,3]

print(x == y) # true
print(x is y) # false

## not é praticamente o sinal de exclamação no js (!false)
print(not False) # true
print((not False) == (False)) # false
print(not (not False)) # false
