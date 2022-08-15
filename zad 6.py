#Ask the user for a string and print out whether this string is a palindrome
#or not. (A palindrome is a string that reads the same forwards and backwards.)


pali = input("podaj jakieś słowo: ")
rvs = pali[::-1]

if pali == rvs:
    print("\n To słowo jest palidromem!")
else:
    print("\n To słowo NIE jest palidromem.")
