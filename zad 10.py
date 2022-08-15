import random

a = []
b = []

for x in range(random.randint(3,55)):
    a.append(random.randint(1,99))
    
for y in range(random.randint(3,55)):
    b.append(random.randint(1,99))

c = []
duplikaty = []
for x in a:
    for y in b:
        if x == y:
            if y in c:
                duplikaty.append(y)
            else:    
                c.append(y)
print("\n")
print("To jest lista A:")            
print(a)
print("\n")
print("To jest lista B:")
print(b)
print("\n")
print("Obie listy zawierają elementy:")  
print(c)
print("\n")
print("wystąpiły duplikaty")  
print(duplikaty)
