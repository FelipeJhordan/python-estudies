astring = "Hello world!"

## imprimir tamanho
print(len(astring))

## mostrar a posição que se encontra determinada string
print(astring.index("o"))

## Contar quantas vezes certo valor aparece na string
print(astring.count("1"))

# Fazer um fatiamento de strings
print(astring[3:7])

### [START:STOP:STEP]
print(astring[3:7:2])

### Como fazer um reverse na string
print(astring[::-1])

## UPPER E lower
print(astring.lower())
print(astring.upper())

## Ver se começa com tal valor ou o contrário
print(astring.startswith("Hello"))
print(astring.endswith("asdsadsadksaofd"))