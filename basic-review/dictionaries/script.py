# Dicionários 
# É semelhante a um array, mas trabalha como chaves, valores ao invez de 
# index, valor.
phonebook = {}
phonebook["John"]=938477566
phonebook["Jack"]=934324324
print(phonebook)

# Também da para inicializar dicionários com a seguinte escrita..
## OBS-> Javascript deixa tudo flexível em, pqp
phonebook = {
    "John": 93298441984,
    "Felipe": 3124234523423423
}

print(phonebook)


# Dá para iterar um dicionário, porém ele não mantêm a ordem dos valores 
# guardados

phonebookIter = phonebook
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Remover um item do dicionário pela chave
del phonebook["Felipe"]
print(phonebook)

phonebook.pop("John")