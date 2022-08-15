#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
#(using input), compare them, print out a message of congratulations
#to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock


import random
print("Zagrajmy w kamień, papier i nożyce! Wpisz KONIEC aby zakończyć")
g1 = 0
k1 = 0

while True:
    print("\n")
    print("PUNKTACJA:")
    print("GRACZ    " + str(g1) + " : " + str(k1) + "    KOMPUTER")
    komputer = 0

    gen = random.randint(1,3)
    if gen == 1:
        komputer = str("kamień")
    elif gen == 2:
        komputer = str("papier")
    elif gen == 3:
        komputer = str("nożyce")
   
    gracz = input("kamień, papier czy nożyce? ")

    if gracz == "KONIEC":
        if g1 > k1:
            print("WYGRAŁEŚ!")
        elif k1 > g1:
            print("PRZEGRAŁEŚ!")
        elif g1 == k1:
            print ("REMIS!")
            
        print("Dziękuję za grę!")
        break

    elif gracz == "kamień" and komputer == "papier":
        k1 = int(k1) +1
        print("PRZEGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "kamień" and komputer == "nożyce":
        g1 = int(g1) +1
        print("WYGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "kamień" and komputer == "kamień":
        print("REMIS! Komputer wybrał " + komputer)
    elif gracz == "papier" and komputer == "papier":
        print("REMIS! Komputer wybrał " + komputer)
    elif gracz == "papier" and komputer == "kamień":
        g1 = int(g1) +1
        print("WYGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "papier" and komputer == "nożyce":
        k1 = int(k1) +1
        print("PRZEGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "nożyce" and komputer == "kamień":
        k1 = int(k1) +1
        print("PRZEGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "nożyce" and komputer == "papier":
        g1 = int(g1) +1
        print("WYGRAŁEŚ! Komputer wybrał " + komputer)
    elif gracz == "nożyce" and komputer == "nożyce":
        print("REMIS! Komputer wybrał " + komputer)
        
    
