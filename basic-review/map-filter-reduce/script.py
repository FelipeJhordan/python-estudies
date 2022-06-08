# Map
## Array
itens = [1,2,3,4,5]

double = list(map(lambda x: x*2, itens))
print(double)

## Dicionários
accounts = [{"name": "João", "balance": 500}, {"name": "Felipe","balance": 42 }]
print(list(map(lambda x: x["balance"] > 1000, accounts)))

# Reduce ( forma semelhante ao js, porém tem que importar a lib-interna functols)
from functools import reduce
soma = reduce((lambda x, y: x+y), [1,2,3,4])
print(soma)

lista = [1,2,3,4,5,6]
maior = reduce((lambda x,y: x if(x>y) else y), lista)
print(maior)

# filter

numeros_pares = list(filter(lambda x: x % 2 == 0, lista))
print(numeros_pares)

