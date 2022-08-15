#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user. Hint: how does an even /
#odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num)
#and one number to divide by (check). If check divides evenly into num,
#tell that to the user. If not, print a different appropriate message.

liczba = int(input("Podaj liczbę: "))
parzyste = liczba % 2
pocztery = liczba % 4
if parzyste == 0:
    print("Ta liczba jest parzysta!")
    if pocztery == 0:
        print("Ta liczba jest także podzielna przez 4!")
    else:
        print("Ta liczba nie dzieli się przez 4.")
else:
    print("Ta liczba jest nieparzysta!")

print("\n")
print("\n")
print("Poproszę Cię jeszcze o dwie liczby. Sprawdzę czy liczba 1 jest podzielna przez liczbę 2")
print("\n")
num = int(input("Liczba 1: "))
check = int(input("Liczba 2: "))
x = num % check
if x == 0:
    print("Liczba 1 jest podzielna przez drugą!")
else:
    print("Liczba 1 nie dzieli się przez liczbę 2")

