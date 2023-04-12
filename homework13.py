#no valid email
# gg@@gg.net больше 2 собак и 2 точек
# @gg@gg.net Собака в начале
# gg@net. точка в конце

# valid email
# gg@gg.net

string_email = input("Enter email: ") # enter emai
a = list(string_email)

if a.count("@") > 1 or a.count(".") > 1 or a[0] == "@" or a[-1] == "." or a.index("@") > a.index("."):
    print("False")
else:
    print("True")
