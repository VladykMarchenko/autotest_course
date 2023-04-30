file = open('txt.txt')
max_word = ''
for line in file:
    words = line.split()
    for word in words:
        if len(word) > len(max_word):
            max_word = word
print(max_word)
