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


#Такие вещи лучше не хардкодить, а выносить в константы или переменные

# if number >= 3 and number <= 6:
#
#
# Элементы списка и так уже числа, поэтому еще раз конвертировать смысла нет, тем более если там будет флоат?
#
# product = (int(lst2[0]) * int(lst2[1]) * int(lst2[2]) * int(lst2[3]))
#
#
# Основной момент, код не работает, если в отфильтрованном списке будет не 4 элемента




