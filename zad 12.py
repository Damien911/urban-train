def krancelisty(lista):
    return [lista[0], lista[len(lista)-1]]

def krancelisty2(lista):
    return [lista.pop(0), lista.pop()]
b = [5, 10, 15, 20, 25]
c = krancelisty(lista = b)
d = krancelisty(lista = b)
print(b)
print(c)
print(d)
