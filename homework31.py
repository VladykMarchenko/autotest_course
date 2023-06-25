import random
def get_random_string(length: int):
    result = ""
    for i in range(length):
        random_num = random.randint(0, 61)
        if random_num < 26:
            result += chr(random_num + 65)
        elif random_num < 52:
            result += chr(random_num + 71)
        else:
            result += chr(random_num - 4)
    return result

print(get_random_string(71))




# random.shuffle сверху закинуть для перемещивания списка

