lst = [3.5, 2, 4, 6.2, 8]

target = []

for index, item in enumerate(lst): # распаковка кортежа, где есть индекс и значение
    # print(index, item)
    target.append(item)
    # print(target)
    if index < len(lst) -1:
        target.append((lst[index +1] + lst[index]) / 2)
print(target)