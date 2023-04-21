lst = [2, 4, 6, 2, 1, 1, 9, 4, 6] #MIN = 3, MAX = 6
MIN = 3
MAX = 6

sum_ = 0
product = 1
for number in lst:
    if number >= MIN and number <= MAX:
        sum_ += number
        product *= number
print(sum_)
print(product)


