#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they
#guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken,
#and when the game ends, print this out.


import random

print("Zagrajmy w typowanie! Poproszę Cię zaraz o podanie liczby od 1 do 999 i sprawdzimy czy komputer wylosował to samo.")
number = random.randint(1,999)
proba = 0
while True:
    
     
    typ = input("Podaj typ: ")
    if typ == "KONIEC":
        print("Dzięki za grę!")
        break

    elif int(typ) < number:
        proba = int(proba + 1)
        print("ZA MAŁO!")
    elif int(typ) > number:
        proba = int(proba + 1)
        print("ZA DUŻO!")
    elif int(typ) == number:
        proba = int(proba + 1)
        print("BINGO!")
        print("Liczba prób: " + str(proba))
        proba = 0
        number = random.randint(1,9)
        print("\n")
