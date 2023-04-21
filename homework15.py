lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
lst2 = []
for number in lst:
    if number >= 3 and number <= 6:
        lst2.append(number)
sum_ = sum(lst2)
product = (int(lst2[0]) * int(lst2[1]) * int(lst2[2]) * int(lst2[3]))
print(sum_)
print(product)



