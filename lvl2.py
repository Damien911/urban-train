#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

seq = []
qwe = []
def silnia(x):
    if x == 0:
        return 1
    else:
        return x * silnia(x - 1)

def pytanie():
    number = 0
    while number is not "end":
        number = input("put a numbers to compute factorial, when u finished, write:  end ")
        if number == "end":
            number = 1
            number = int(number)
            break
        else:
            number = int(number)
            qwe.append(number)
    proces(qwe)

def proces(qwe):
    for i in qwe:
        geg = silnia(i)
        int(geg)
        seq.append(geg)
    
        
        

    
start = pytanie()

print(qwe)

print(seq)
    
