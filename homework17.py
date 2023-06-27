lst = [['a', 'c', 'd'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

transposed = list(zip(*lst))
sorted_transposed = [sorted(row) for row in transposed]
result = [list(row) for row in zip(*sorted_transposed)]
for i in result:
    print(i)
