#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.
#Hints:
#Use __init__ method to construct some parameters

class klasa():

    def __init__(self):
        self.inp = ""
        self.out = ""
    def getString(self):
        self.inp = input("Please type something ")
               
    def printString(self):
        self.out = self.inp.upper()
        print(self.out)

    def test(self):
        if self.inp != self.out:
            print("OK!")
        else:
            print("ERROR!")

start = klasa()
start.getString()
start.printString()
start.test()

