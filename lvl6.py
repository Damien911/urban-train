#Write a program that calculates and prints the value
#according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program
#in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence
#is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

#Hints:
#If the output received is in decimal form, it should be rounded off
#to its nearest value (for example, if the output received is 26.0,
#                      it should be printed as 26)
#In case of input data being supplied to the question,
#it should be assumed to be a console input.
import math

class calc():

    def __init__(self):

        self.C = 50
        self.H = 30
        self.D = ""
        
    def input(self):

        self.D = int(input("Give a value: "))

    def pro(self):
        
        output = math.sqrt((2 * self.C * self.D)/ self.H)
        output = int(output)
        self.out = output

    def pri(self):

        print(self.out)

    def test(self):
        self.D = int(100)
        start.pro()
        if self.D == 100 and self.out == 18:
            print("100 -> 18  OK!")

        self.D = int(150)
        start.pro()
        if self.D == 150 and self.out == 22:
            print("150 -> 22 OK!")

        self.D = int(180)
        start.pro()
        if self.D == 180 and self.out == 24:
            print("180 -> 24 OK!")

start = calc()
start.input()
start.pro()
start.pri()
start.test()
        
