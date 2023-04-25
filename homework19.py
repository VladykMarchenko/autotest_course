users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

t = []

for i in users:
    if i["age"] >= 18:
        t.append(i['name'])
print(t)
