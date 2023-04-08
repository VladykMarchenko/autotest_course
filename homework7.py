

a = input("vibrat ")
height = int(a)
symbol = input("Enter symbol: ")
for row_level in range(height):
    string = '' # крайнее поле слева, в данном случае пустое
    for left_step in range(height - row_level): # управляем направление +\-
        string += ' '
        string += symbol
    print(string)




