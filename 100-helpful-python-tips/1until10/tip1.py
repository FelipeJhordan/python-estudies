# Caso o loop rode ate o final, o código dentro da clausula é rodado

numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")
