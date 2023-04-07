a = input("Enter height of rectangular: ")
b = input("Enter width of rectangular: ")
symbol = input("choose symbol: ")
if a and b:
    height = int(a)
    width = int(b)
    for row in range(1, height +1):
        print(width * symbol)