multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
multi_string2 = multi_string.split('.') # разбиваем строчку на предложения
words_number = []
for sentence in multi_string2:
    words = sentence.split(' ')  # циклом проходимся по каждому предложению и разбиваем на слова
    count = 0
    for word in words:
        if word != '':
            count += 1
    words_number.append(count)
print(words_number[:-1])

