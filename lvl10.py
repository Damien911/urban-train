#Write a program that accepts a sequence of whitespace separated words
#as input and prints the words after removing all duplicate words
#and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

#Hints:
#In case of input data being supplied to the question,
#it should be assumed to be a console input.
#We use set container to remove duplicated data automatically
#and then use sorted() to sort the data.

class klasa ():

    def __init__ (self):

        klasa.inp(self)
        print(self.string2)

    def inp(self):
        
        inpu = input("Input a sequence of whitespace separeted words ")
        inpu = inpu.split(" ")
        deleting = set(inpu)
        deleting = sorted(deleting)
        string2 = " ".join(deleting)
        self.string2 = string2


start = klasa()


        

    
