t = []
with open('txt.txt') as f:
    for i, line in enumerate(f):
            t.append(line)
print(sorted(str(input(line).split()[-1])))







