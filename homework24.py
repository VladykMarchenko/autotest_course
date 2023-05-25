def second_largest_number(lst):
    if lst == []:
        return
    first, second, *_array = lst
    if not second:  # or not _array
        return second
    if first < second:
        first, second = second, first
    for current in _array:
        if current > first:
            second, first = first, current
        elif first > current > second:
            second = current
    return second

a = second_largest_number([5,2,3,4,5,6,97,45])
print(a)


