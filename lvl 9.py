#Write a program that accepts sequence of lines as input
#and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

#Hints:
#In case of input data being supplied to the question,
#it should be assumed to be a console input.

class klasa():

    def __init__(self):
        self.x1 = ""
        self.x2 = ""
        klasa.inp(self)
        klasa.out(self)
        klasa.pri(self)

    def inp(self):

        self.x1 = input("type a text: ")
        self.x2 = input("Please type a text again: ")
        

    def out(self):

        self.x1 = self.x1.upper()
        self.x2 = self.x2.upper()

    def pri(self):

        print(self.x1)
        print(self.x2)

start=klasa()
