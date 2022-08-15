#Write a program that accepts a comma separated sequence
#of words as input and prints the words in a comma-separated
#sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

#Hints:
#In case of input data being supplied to the question,
#it should be assumed to be a console input.

class klasa ():

    def __init__(self):
        
        self.inp = ""
        self.sorted = ""
        klasa.inpu(self)
        klasa.printing(self)
        
    
    def inpu(self):

        inp = input("Write a come separated sequence of words ")
        lista = inp.split(",")
        self.sorted = sorted(lista)
        self.sorted = ",".join(self.sorted)
        
    def printing(self):

        print(self.sorted)
        
start = klasa()
