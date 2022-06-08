# For

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range(5):
    print(x)

# While
count = 0
while count < 5:
    print(count)
    count += 1

## Que po54 é essa?
## else no loop
## Caso nenhum "break" seja acionado dentro da itereção, o 
## código dentro do else será ativado
for i in range(3):
    if(i > 5):
        break
else:
    print("Else Statements")