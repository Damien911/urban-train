listaaa = []

def generator (zakres):
    x = 0
    for i in range(zakres):
        x = x + 1
        listaaa.append(x)
liczba = input("ile liczb wygenerować ? ")
liczba = int(liczba)
generator(liczba)
print(listaaa)

def wyszBinarne(lista, item):
    low = 0
    high = len(lista)-1
    ileprob = 0
    while low <= high:
        ileprob = ileprob + 1
        mid = (low + high)/2
        mid = int(mid)
        
        guess = lista[mid]
        if guess == item:
            
            print(ileprob)
            print(mid)
            return mid
            
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            return None

propozycja = int(input("Który element wyszukać? "))

wyszBinarne(listaaa, propozycja)
