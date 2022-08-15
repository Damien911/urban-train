def Fibo(help_text = "ile liczb wygenerować ? "):
    ile = int(input(help_text))
    a = [1,1]
    if ile > 1:
        for x in range(ile):
            b = a[len(a)-1] + a[len(a)-2]
            a.append(b)           
        return a
    elif ile == 1:
        return 1
    elif ile == 0:
        return 0
    else:
        print("Potrzebna jest liczba całkowita")
    
y = Fibo()
print(y)
