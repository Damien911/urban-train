def gameBoard():
    print("What size of a board do you want to create?")
    width = int(input("please define width of a board "))
    height = int(input("please define hight of a board "))

    for x in range(height):
        print(" ---" * width)
        print("|   " * (width +1))
    print(" ---" * width)
heh = gameBoard()
