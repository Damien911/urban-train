#Write a program which takes 2 digits, X,Y as input and generates
#a 2-dimensional array. The element value in the i-th row and j-th column
#of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

#Hints:
#Note: In case of input data being supplied to the question,
#it should be assumed to be a console input in a comma-separated form.
import numpy as np

class tabelka():

    def __init__(self):

        tabelka.inp(self)
        tabelka.test(self)
        tabelka.create(self)
    
    def inp(self):

        inp = input("type two single digits ")
        inp = list(inp)
        ile = inp.count(",")
        for k in range (ile):
            inp.remove(",")

        self.x = inp[0]
        
        self.y = inp[1]
        print(inp)

    def create(self):
        lista = []
        x2 = int(self.x)
        y2 = int(self.y)
        
        t = [ [0]*y2 for i in range(x2)]
             
        for h in range(x2):
            for k in range(y2):
                t[h][k]= h*k

        print(t)

        return t
                
    def test(self):
        
        print(self.x)
        print(self.y)
                      
start = tabelka()

