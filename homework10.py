# "    aBC cba " # True
# "a BCQcb a    " # True
# " ab bca"  # False

str1 = input("Enter polidron1: ")
str3 = str1.lower().strip()
if str3 == str3[::-1]:
    print("true")
else:
    print("false")

if str3 == "".join(reversed(str3)):
    print("true")
else:
    print("false")
