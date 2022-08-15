import random


liczba = []
liczba1 = []
liczbaGracza = []
liczbaGracza1 = []
krowy = 0
byki = 0

def generatorLiczb():
    losowanie = random.randint(0, 9999)
    global liczba
    liczba = str(losowanie)
    liczba = list(liczba)
    if losowanie >= 0 and losowanie < 10:
        liczba.insert(0, 0)
        liczba.insert(0, 0)
        liczba.insert(0, 0)
    elif losowanie >= 10 and losowanie < 100:
        liczba.insert(0, 0)
        liczba.insert(0, 0)
    elif losowanie >= 100 and losowanie < 1000:
        liczba.insert(0, 0)
    for y in liczba:
        liczba1.append(int(y))
    print(liczba)
    print(liczba1)
    print(losowanie)

def typ():
    global liczbaGracza
    liczbaGracza = input("Podaj jakąś liczbę w zakresie 0-9999: ")
    liczbaGracza = list(liczbaGracza)
    for y in liczbaGracza:
        liczbaGracza1.append(int(y))
    print(liczbaGracza1)

def sprawdzanie(liczba1, liczbaGracza1):
    global krowy, byki
    while True:
        for i in liczba1:
            if liczba1 == liczbaGracza1:
                krowy = krowy +1
        for i in liczba1:
            for x in liczbaGracza1:
                if liczba1 in liczbaGracza1 and liczba1 == liczbaGracza1:
                    byki = byki +1
        print(krowy, " krów, ", byki, " byków")
        if krowy == 4:
            break
        else:
            liczbaGracza1.clear()
            typ()
                
            
            
generatorLiczb()
print(liczba)
typ()
print(liczbaGracza)
sprawdzanie(liczba1, liczbaGracza1)
