#Create a program that asks the user for a number and then prints out
#a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly
# into another number. For example, 13 is a divisor of 26 because 26 / 13
# has no remainder.)

a = []
number = int(input("Podaj liczbę: "))

for i in range(number):
    b = number % (i + 1) 
    if b == 0:
        a.append(i + 1)
print("\n")
print("Podana liczba dzieli się przez: \n")
print(a)
