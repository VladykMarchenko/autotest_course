rows = int(input("Введите шото: "))
shift = rows - 1
for i in range(1, rows + 1):
    print('  ' * shift, end='')
    shift -= 1
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()









