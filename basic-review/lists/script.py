# Listas são semelhantes a arrays
# Da para construir semelhante ao js
# A função de adicionar é list.append
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist[1] = 11

for x in mylist:
    print(x)


# Acessar uma posição que não foi populada da erro ( obvio )
# print(mylist[12])
# IndexError: list index out of range