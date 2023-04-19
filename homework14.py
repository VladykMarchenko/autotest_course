lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
lst2 = []
lst3 = []
lst4 = []
# [3, 6, 9, 12]  # elements divided by 3
# [5, 10]  # elements divided by 5
# [0, 15]  # elements divided by 3 and by 5
for number in lst:
    if number % 3 == 0  and number % 5 > 0:
        lst2.append(number)
print(lst2)

for number in lst:
    if number % 5 == 0 and number % 3 > 0:
        lst3.append(number)
print(lst3)

for number in lst:
    if number % 3 == 0 and number % 5 == 0:
        lst4.append(number)
print(lst4)


