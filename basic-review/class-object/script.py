## Como criar uma classe
class MyClass:
    variable = "blah blah"

    def function(self):
        print("This is a message inside the class.")

## Como instanciar
myobjectx = MyClass()
myobjectx.function()
print(myobjectx.variable)

## Construtor
## Self -> this em js
class NumberHolder:
    def __init__(self, number):
        self.number = number

n = NumberHolder(21)
print(n.number)