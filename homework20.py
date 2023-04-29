t = []
with open('txt.txt') as f:
    for i, line in enumerate(f):
        if line != 0:
            t.append(line)
print(sorted(str(input(line).split()[-1])))







