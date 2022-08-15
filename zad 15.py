
zdanie = input("Napisz jakieś kilkuwyrazowe zdanie. ")
def zadanie(zdanie):
    podzielone = zdanie.split(" ")
    odwrocone =  podzielone[::-1]
    polaczone = " ".join(odwrocone)
    print(podzielone)
    print(odwrocone)
    print(polaczone)
zadanie(zdanie)
