def to_dict(lst):
    key = []
    value = []
    for v in lst:
        if v % 2 == 0:
            value.append(v)
        else:
            key.append(v)
    result_2_raw = zip(key, value)
    new_result = dict(result_2_raw)
    print(new_result)
    return new_result
list_for_checking = list(range(10))
to_dict(list_for_checking)

