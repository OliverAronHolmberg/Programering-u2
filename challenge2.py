def Square_Maker(symbol, length, height):
    for x in range(height):
        for y in range(length):
            print(symbol + " ", end="")
        print("")

symbol = input("Enter a symbol: ")

length = int(input("Enter a length: "))
height = int(input("Enter a height: "))

Square_Maker(symbol, length, height)
