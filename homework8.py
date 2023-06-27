# min_width = int(input("Enter minimal width: "))
# max_width = int(input("Enter maximal width: "))
#
# if min_width > max_width:
#     print("Minimal width cannot be greater than maximal width.")
# elif (max_width - min_width) % 2 != 0:
#     print("Difference between maximal and minimal width must be even.")
# else:
#     diamond = []
#     for i in range(min_width, max_width + 1):
#         row = ["*"] * i
#         if i != max_width:
#             row[(i - 1) // 2] = " "
#         diamond.append("".join(row))
#     diamond += diamond[-2::-1]
# print("".join(diamond))


def diamond_pattern(min_width, max_width):
    if min_width > max_width:
        print("Minimal width cannot be greater than maximal width.")
        return

    if (max_width - min_width) % 2 != 0:
        print("Difference between maximal and minimal width must be even.")
        return

    for i in range(min_width, max_width + 1, 2):
        print(" " * ((max_width - i) // 2) + "*" * i)
    for i in range(max_width - 2, min_width - 1, -2):
        print(" " * ((max_width - i) // 2) + "*" * i)

# примеры использования
diamond_pattern(3, 5)
diamond_pattern(1, 3)
diamond_pattern(2, 6)
diamond_pattern(3, 9)