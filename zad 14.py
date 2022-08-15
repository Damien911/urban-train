import random

lista = []
druga = []
def pierwsza(ile):
    global lista
    global druga
    for x in range(ile):
        lista.append(random.randint(1,5))
    for i in lista:
        if i not in druga:
            druga.append(i)
ile = int(input("Ile liczb wygenerować ? "))

pierwsza(ile)

print("Funkcja z For i If")
print(lista)
print(druga)
trzecia = set()
czwarta = []
def drugaa(ile):
    global trzecia
    for x in range(ile):
        trzecia.add(random.randint(1,5))
    trzecia = list(trzecia)
drugaa(ile)
print("sety")
print(trzecia)
