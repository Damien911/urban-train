def mianowniki(help_text = "Podaj liczbę: "):
    a = []
    number = int(input(help_text))

    for i in range(number):
        b = number % (i + 1) 
        if b == 0:
            a.append(i + 1)
    return a

miano = mianowniki(help_text = "podaj liczbę całkowitą: ")
print("\n")
print("Podana liczba dzieli się przez: \n")
print(miano)
hehe = len(miano)
print(hehe)
if hehe == 2:
    print(hehe, "jest liczbą pierwszą")

else:
    print(hehe, "NIE jest liczbą pierwszą")

