import random

def generator(trudnosc):
    alfabet = ("a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P Q R S Ś T U V W X Y Z Ź Ż 1 2 3 4 5 6 7 8 9 0")
    symbole = alfabet.split(" ")
    znaki = random.sample(symbole, trudnosc)
    haslo = "".join(znaki)
    print(haslo)
    
trudnosc = int(input("ile znaków ma posiadać hasło? "))
generator(trudnosc)

    
