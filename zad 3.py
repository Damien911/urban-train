#Take a list, say for example this one:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements
#of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one,
#make a new list that has all the elements less than 5
#from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains
#only elements from the original list a that are smaller
#than that number given by the user.

import random

a = []
b = []
c = []

print("Za chwilę poproszę Cię o kilka danych do wygenerowania listy \n")
minimum = int(input("Najniższy zakres generowanych liczb: "))
maximum = int(input("Najwyższy zakres generowanych liczb: "))
ile = int(input("ile liczb ma zawierać lista: "))

for i in range (ile):
    a.append(random.randint(minimum,maximum))
x = int(input("Podaj liczbę: "))
for element in a:
    if element > 5:
        b.append(element)

for element in a:
    if element < x:
        c.append(element)
          
print("\n Wygenerowana lista to: ")        
print(a)
print("\n Liczby większe od 5 w wygenerowanej liście to: ")          
print(b)
print("\n Liczby mniejsze niż " + str(x) + " w wygenerowanej liście to: ")
print(c)
