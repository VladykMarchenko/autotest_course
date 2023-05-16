def read_last(file_path, symbol_number):
    open_file = open(file_path).readlines()
    for file in open_file:
        if file.strip() != "":
            print(file.strip()[-symbol_number:])
read_last('read_last.txt', 6)
















# file1 = open('read_last.txt')
# stroka1 = file1.readline().split('\n')
# print(stroka1[0])
#
# pp = file1.read().split('\n') # убирает пос
# print(pp)
# for lane in pp:
#     print(lane)

# char_list = []  # объявляем пустой список
# string = 'май'
# for c in string: # идем по строке
#     char_list.append(c) # добавляем буквы в список
# print(char_list)  # >>>> ['м', 'а', 'й']

# def perform_login(username, password): # perform_login это сигнатура
#     pass   # pass это инструкция или ключевое слово
# print(perform_login('1','2'))
#
#



