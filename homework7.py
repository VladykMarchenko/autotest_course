height = int(input("vibrat "))
symbol = input("Enter symbol: ")
for row in range(1, height +1):
    print(" " * (height-row) + symbol * row)
